"""Serviço de integração com a API pública OpenSky Network.

Este módulo expõe a classe :class:`OpenSkyService`, responsável por consultar
dados de tráfego aéreo em tempo real e histórico junto à API do OpenSky
Network (https://opensky-network.org/apidoc/), reaproveitando uma única
sessão HTTP e nunca propagando exceções para o código chamador.

Exemplo de uso:
    >>> from services.opensky_service import OpenSkyService
    >>> service = OpenSkyService()
    >>> resultado = service.buscar_voos()
    >>> if resultado.success:
    ...     print(resultado.data.head())
    >>> service.fechar()

    # Ou como context manager:
    >>> with OpenSkyService() as service:
    ...     resultado = service.buscar_voo_por_icao24("3c675a")
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from types import TracebackType
from typing import Any, Optional

import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import (
    ConnectionError as RequestsConnectionError,
    HTTPError,
    RequestException,
    Timeout,
)

logger = logging.getLogger(__name__)


# --------------------------------------------------------------------------- #
# Constantes de configuração
# --------------------------------------------------------------------------- #
BASE_URL: str = "https://opensky-network.org/api"
DEFAULT_TIMEOUT: float = 10.0
DEFAULT_HISTORICO_HORAS: int = 2

ENV_USERNAME: str = "OPENSKY_USERNAME"
ENV_PASSWORD: str = "OPENSKY_PASSWORD"

# Ordem oficial das colunas de um "state vector" da API OpenSky.
# Referência: https://openskynetwork.github.io/opensky-api/rest.html
STATE_VECTOR_COLUMNS: tuple[str, ...] = (
    "icao24",
    "callsign",
    "origin_country",
    "time_position",
    "last_contact",
    "longitude",
    "latitude",
    "baro_altitude",
    "on_ground",
    "velocity",
    "heading",
    "vertical_rate",
    "sensors",
    "geo_altitude",
    "squawk",
    "spi",
    "position_source",
)


@dataclass
class OpenSkyResult:
    """Objeto de retorno padronizado para todas as operações do serviço.

    Usar um objeto de resultado único (ao invés de lançar exceções ou
    retornar tipos variados) permite que o código chamador sempre trate a
    resposta da mesma forma, verificando apenas o atributo ``success``.

    Attributes:
        success: Indica se a operação foi concluída com sucesso.
        data: Payload retornado (DataFrame, dict, list etc.) quando
            ``success`` for ``True``.
        error: Mensagem de erro legível quando ``success`` for ``False``.
        status_code: Código HTTP retornado pela API, quando aplicável.
    """

    success: bool
    data: Any = None
    error: Optional[str] = None
    status_code: Optional[int] = None

    @classmethod
    def ok(cls, data: Any, status_code: Optional[int] = None) -> "OpenSkyResult":
        """Cria um resultado de sucesso."""
        return cls(success=True, data=data, status_code=status_code)

    @classmethod
    def fail(cls, error: str, status_code: Optional[int] = None) -> "OpenSkyResult":
        """Cria um resultado de falha, sem lançar exceção."""
        return cls(success=False, error=error, status_code=status_code)


class OpenSkyService:
    """Cliente reutilizável para a API pública do OpenSky Network.

    A classe encapsula a criação e o reaproveitamento de uma
    ``requests.Session``, autenticação opcional via variáveis de ambiente,
    timeout configurável e tratamento centralizado de exceções de rede.

    Nenhum método desta classe lança exceções para o chamador: todas as
    operações retornam um :class:`OpenSkyResult`, indicando sucesso ou falha.

    Attributes:
        base_url: URL base da API OpenSky.
        timeout: Timeout padrão (em segundos) aplicado às requisições.
    """

    def __init__(
        self,
        base_url: str = BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ) -> None:
        """Inicializa o serviço e a sessão HTTP subjacente.

        Args:
            base_url: URL base da API. Permite apontar para um mock/proxy
                em ambientes de teste.
            timeout: Timeout padrão, em segundos, para as requisições.
            username: Usuário OpenSky. Se omitido, é lido da variável de
                ambiente ``OPENSKY_USERNAME``.
            password: Senha OpenSky. Se omitida, é lida da variável de
                ambiente ``OPENSKY_PASSWORD``.
        """
        self.base_url: str = base_url.rstrip("/")
        self.timeout: float = timeout
        self._session: requests.Session = requests.Session()
        self._auth: Optional[HTTPBasicAuth] = self._build_auth(username, password)

        if self._auth is not None:
            logger.info("OpenSkyService inicializado com autenticação de usuário.")
        else:
            logger.info("OpenSkyService inicializado em modo anônimo (sem autenticação).")

    # --------------------------------------------------------------------- #
    # Configuração / infraestrutura
    # --------------------------------------------------------------------- #
    @staticmethod
    def _build_auth(
        username: Optional[str], password: Optional[str]
    ) -> Optional[HTTPBasicAuth]:
        """Monta as credenciais HTTP Basic a partir de argumentos ou do ambiente.

        Args:
            username: Usuário informado explicitamente (tem prioridade).
            password: Senha informada explicitamente (tem prioridade).

        Returns:
            Um ``HTTPBasicAuth`` pronto para uso, ou ``None`` caso não haja
            credenciais completas disponíveis.
        """
        user = username or os.getenv(ENV_USERNAME)
        pwd = password or os.getenv(ENV_PASSWORD)
        if user and pwd:
            return HTTPBasicAuth(user, pwd)
        return None

    def _request(
        self,
        endpoint: str,
        params: Optional[dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> OpenSkyResult:
        """Executa uma requisição GET à API, tratando todas as exceções.

        Centralizar a chamada HTTP aqui evita duplicação de blocos
        try/except em cada método público e garante um comportamento
        consistente de logging e de retorno de erros.

        Args:
            endpoint: Caminho relativo do endpoint (ex.: ``"/states/all"``).
            params: Parâmetros de query string opcionais.
            timeout: Timeout específico para esta chamada; se ``None``,
                usa ``self.timeout``.

        Returns:
            ``OpenSkyResult`` com o JSON decodificado em ``data`` em caso
            de sucesso, ou com a mensagem de erro em ``error`` caso
            contrário.
        """
        url = f"{self.base_url}{endpoint}"
        effective_timeout = timeout if timeout is not None else self.timeout

        try:
            response = self._session.get(
                url,
                params=params,
                auth=self._auth,
                timeout=effective_timeout,
            )
            response.raise_for_status()
            return OpenSkyResult.ok(response.json(), status_code=response.status_code)

        except Timeout:
            msg = (
                f"Tempo limite excedido ao acessar '{url}' "
                f"(timeout={effective_timeout}s)."
            )
            logger.error(msg)
            return OpenSkyResult.fail(msg)

        except HTTPError as exc:
            status = exc.response.status_code if exc.response is not None else None
            msg = f"Erro HTTP {status} ao acessar '{url}': {exc}"
            logger.error(msg)
            return OpenSkyResult.fail(msg, status_code=status)

        except RequestsConnectionError:
            msg = (
                f"Falha de conexão ao acessar '{url}'. "
                "Verifique sua rede ou a disponibilidade da API OpenSky."
            )
            logger.error(msg)
            return OpenSkyResult.fail(msg)

        except RequestException as exc:
            msg = f"Erro inesperado de requisição ao acessar '{url}': {exc}"
            logger.error(msg)
            return OpenSkyResult.fail(msg)

        except ValueError as exc:
            # response.json() lança ValueError quando o corpo não é JSON válido.
            msg = f"Resposta inválida (JSON malformado) recebida de '{url}': {exc}"
            logger.error(msg)
            return OpenSkyResult.fail(msg)

    # --------------------------------------------------------------------- #
    # Validação / transformação de dados
    # --------------------------------------------------------------------- #
    @staticmethod
    def _states_payload_to_dataframe(payload: Any) -> Optional[pd.DataFrame]:
        """Converte e valida o payload de ``/states/all`` em um DataFrame.

        Garante que o payload tem o formato esperado antes de montar o
        DataFrame, e descarta silenciosamente (com aviso em log) linhas
        cujo número de colunas não bate com ``STATE_VECTOR_COLUMNS`` —
        isso evita o erro clássico de "ValueError: shape mismatch" quando
        a API muda o formato de alguns registros.

        Args:
            payload: Corpo JSON decodificado da resposta da API.

        Returns:
            Um DataFrame com as colunas de ``STATE_VECTOR_COLUMNS``, ou
            ``None`` se o payload não tiver o formato mínimo esperado.
        """
        if not isinstance(payload, dict) or "states" not in payload:
            return None

        states = payload.get("states")
        if states is None:
            return pd.DataFrame(columns=STATE_VECTOR_COLUMNS)

        if not isinstance(states, list):
            return None

        num_colunas = len(STATE_VECTOR_COLUMNS)
        linhas_validas = [
            linha
            for linha in states
            if isinstance(linha, list) and len(linha) == num_colunas
        ]

        descartadas = len(states) - len(linhas_validas)
        if descartadas:
            logger.warning(
                "Descartada(s) %d linha(s) de 'states' com número de "
                "colunas inconsistente com o esperado (%d).",
                descartadas,
                num_colunas,
            )

        return pd.DataFrame(linhas_validas, columns=STATE_VECTOR_COLUMNS)

    # --------------------------------------------------------------------- #
    # API pública
    # --------------------------------------------------------------------- #
    def buscar_voos(self, timeout: Optional[float] = None) -> OpenSkyResult:
        """Busca o estado atual de todas as aeronaves visíveis pela API.

        Args:
            timeout: Timeout específico para esta chamada (opcional).

        Returns:
            ``OpenSkyResult`` cujo ``data`` é um ``pandas.DataFrame`` com
            as colunas definidas em ``STATE_VECTOR_COLUMNS`` em caso de
            sucesso, ou ``error`` preenchido em caso de falha.
        """
        resultado = self._request("/states/all", timeout=timeout)
        if not resultado.success:
            return resultado

        df = self._states_payload_to_dataframe(resultado.data)
        if df is None:
            msg = (
                "Formato de resposta inesperado da API: chave 'states' "
                "ausente ou com tipo inválido."
            )
            logger.error(msg)
            return OpenSkyResult.fail(msg, status_code=resultado.status_code)

        return OpenSkyResult.ok(df, status_code=resultado.status_code)

    def buscar_historico(
        self,
        icao24: str,
        horas: int = DEFAULT_HISTORICO_HORAS,
        timeout: Optional[float] = None,
    ) -> OpenSkyResult:
        """Busca o histórico de trajetória (track) de uma aeronave.

        Args:
            icao24: Identificador ICAO24 da aeronave (hexadecimal).
            horas: Janela de tempo, em horas, a partir de agora, usada
                como referência inicial da consulta. Padrão: 2 horas.
            timeout: Timeout específico para esta chamada (opcional).

        Returns:
            ``OpenSkyResult`` com o JSON de trajetória em ``data``, ou
            ``error`` preenchido em caso de parâmetros inválidos ou falha
            na API.
        """
        if not icao24 or not isinstance(icao24, str):
            return OpenSkyResult.fail(
                "Parâmetro 'icao24' inválido: deve ser uma string não vazia."
            )
        if horas <= 0:
            return OpenSkyResult.fail("Parâmetro 'horas' deve ser maior que zero.")

        inicio = datetime.now(timezone.utc) - timedelta(hours=horas)
        params = {"icao24": icao24.lower(), "time": int(inicio.timestamp())}

        # Endpoint correto da API pública para consulta de trajetórias.
        return self._request("/tracks/all", params=params, timeout=timeout)

    def buscar_voo_por_callsign(
        self, callsign: str, timeout: Optional[float] = None
    ) -> OpenSkyResult:
        """Filtra, dentre os voos atuais, aquele(s) com o callsign informado.

        Args:
            callsign: Indicativo de chamada da aeronave (ex.: ``"TAM3456"``).
            timeout: Timeout específico para a busca subjacente (opcional).

        Returns:
            ``OpenSkyResult`` com um DataFrame filtrado em ``data``, ou
            ``error`` caso o callsign seja inválido, a busca falhe, ou
            nenhum voo seja encontrado.
        """
        if not callsign or not isinstance(callsign, str):
            return OpenSkyResult.fail(
                "Parâmetro 'callsign' inválido: deve ser uma string não vazia."
            )

        voos = self.buscar_voos(timeout=timeout)
        if not voos.success:
            return voos

        alvo = callsign.strip().upper()
        df = voos.data
        filtrado = df[df["callsign"].astype(str).str.strip().str.upper() == alvo]

        if filtrado.empty:
            return OpenSkyResult.fail(f"Nenhum voo encontrado para o callsign '{callsign}'.")

        return OpenSkyResult.ok(filtrado.reset_index(drop=True))

    def buscar_voo_por_icao24(
        self, icao24: str, timeout: Optional[float] = None
    ) -> OpenSkyResult:
        """Filtra, dentre os voos atuais, aquele com o icao24 informado.

        Args:
            icao24: Identificador ICAO24 da aeronave (hexadecimal).
            timeout: Timeout específico para a busca subjacente (opcional).

        Returns:
            ``OpenSkyResult`` com um DataFrame filtrado em ``data``, ou
            ``error`` caso o icao24 seja inválido, a busca falhe, ou
            nenhum voo seja encontrado.
        """
        if not icao24 or not isinstance(icao24, str):
            return OpenSkyResult.fail(
                "Parâmetro 'icao24' inválido: deve ser uma string não vazia."
            )

        voos = self.buscar_voos(timeout=timeout)
        if not voos.success:
            return voos

        alvo = icao24.strip().lower()
        df = voos.data
        filtrado = df[df["icao24"].astype(str).str.strip().str.lower() == alvo]

        if filtrado.empty:
            return OpenSkyResult.fail(f"Nenhum voo encontrado para o icao24 '{icao24}'.")

        return OpenSkyResult.ok(filtrado.reset_index(drop=True))

    def listar_voos_por_pais(
        self, pais: str, timeout: Optional[float] = None
    ) -> OpenSkyResult:
        """Filtra, dentre os voos atuais, os que pertencem a um país de origem.

        Args:
            pais: Nome (ou parte do nome) do país de origem, ex.:
                ``"Brazil"``. A busca não diferencia maiúsculas/minúsculas
                e aceita correspondência parcial.
            timeout: Timeout específico para a busca subjacente (opcional).

        Returns:
            ``OpenSkyResult`` com um DataFrame filtrado em ``data``, ou
            ``error`` caso o país seja inválido, a busca falhe, ou
            nenhum voo seja encontrado.
        """
        if not pais or not isinstance(pais, str):
            return OpenSkyResult.fail(
                "Parâmetro 'pais' inválido: deve ser uma string não vazia."
            )

        voos = self.buscar_voos(timeout=timeout)
        if not voos.success:
            return voos

        df = voos.data
        filtrado = df[
            df["origin_country"].astype(str).str.contains(pais, case=False, na=False)
        ]

        if filtrado.empty:
            return OpenSkyResult.fail(f"Nenhum voo encontrado para o país '{pais}'.")

        return OpenSkyResult.ok(filtrado.reset_index(drop=True))

    def fechar(self) -> None:
        """Encerra a sessão HTTP subjacente, liberando conexões abertas."""
        self._session.close()
        logger.info("Sessão HTTP do OpenSkyService encerrada.")

    # --------------------------------------------------------------------- #
    # Suporte a uso como context manager
    # --------------------------------------------------------------------- #
    def __enter__(self) -> "OpenSkyService":
        """Permite o uso de ``OpenSkyService`` em um bloco ``with``."""
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        """Garante o fechamento da sessão ao sair do bloco ``with``."""
        self.fechar()