import pandas as pd
from services.opensky_service import OpenSkyService

def exibir_voos_em_tempo_real():
    with OpenSkyService() as service:
        resultado = service.buscar_voos()
        if not resultado.success:
            print(f"\nErro: {resultado.error}")
            return
        df = resultado.data
        if df.empty:
            print("\nNenhum voo ativo no momento.")
            return
        colunas = ['callsign', 'origin_country', 'latitude', 'longitude', 'baro_altitude', 'velocity']
        colunas_existentes = [c for c in colunas if c in df.columns]
        print(f"\nVoos ativos: {len(df)}")
        print(df[colunas_existentes].head(10).to_string(index=False))

def buscar_voo_por_callsign():
    callsign = input("Digite o callsign: ").strip().upper()
    if not callsign:
        print("Callsign inválido.")
        return
    with OpenSkyService() as service:
        resultado = service.buscar_voo_por_callsign(callsign)
        if not resultado.success:
            print(f"\nErro: {resultado.error}")
            return
        df = resultado.data
        print(f"\nVoos encontrados para '{callsign}':")
        print(df.to_string(index=False))

def buscar_voo_por_icao():
    icao = input("Digite o ICAO24: ").strip().lower()
    if not icao:
        print("ICAO24 inválido.")
        return
    with OpenSkyService() as service:
        resultado = service.buscar_voo_por_icao24(icao)
        if not resultado.success:
            print(f"\nErro: {resultado.error}")
            return
        df = resultado.data
        print(f"\nVoo encontrado para ICAO24 '{icao}':")
        print(df.to_string(index=False))

def listar_voos_por_pais():
    pais = input("Digite o país (ex: Brazil): ").strip()
    if not pais:
        print("País inválido.")
        return
    with OpenSkyService() as service:
        resultado = service.listar_voos_por_pais(pais)
        if not resultado.success:
            print(f"\nErro: {resultado.error}")
            return
        df = resultado.data
        print(f"\nVoos com origem em '{pais}': {len(df)}")
        print(df[['callsign', 'origin_country', 'latitude', 'longitude']].head(10).to_string(index=False))

def exibir_submenu_monitoramento():
    while True:
        print("\n" + "-"*40)
        print("    MONITORAMENTO DE VOOS")
        print("-"*40)
        print("1 - Exibir voos em tempo real")
        print("2 - Buscar por callsign")
        print("3 - Buscar por ICAO24")
        print("4 - Listar por país")
        print("0 - Voltar ao menu da torre")
        print("-"*40)
        opcao = input("Escolha: ").strip()
        if opcao == '1':
            exibir_voos_em_tempo_real()
        elif opcao == '2':
            buscar_voo_por_callsign()
        elif opcao == '3':
            buscar_voo_por_icao()
        elif opcao == '4':
            listar_voos_por_pais()
        elif opcao == '0':
            break
        else:
            print("\nOpção inválida!")

def exibir_voos_militares():
    with OpenSkyService() as service:
        resultado = service.buscar_voos()
        if not resultado.success:
            print(f"\nErro: {resultado.error}")
            return
        df = resultado.data
        if df.empty:
            print("\nNenhum voo ativo no momento.")
            return

        padroes_mil = ['AF', 'NAVY', 'ARMY', 'R', 'F', 'MIL', 'GAF', 'RFR', 'RCH']
        paises_mil = ['United States', 'Russian Federation', 'China', 'United Kingdom',
                      'France', 'Germany', 'India', 'Israel', 'Turkey']

        def is_military(row):
            callsign = str(row.get('callsign', '')).upper()
            country = str(row.get('origin_country', ''))
            if any(pad in callsign for pad in padroes_mil):
                return True
            if country in paises_mil:
                return True
            return False

        df['is_military'] = df.apply(is_military, axis=1)
        df_mil = df[df['is_military']].drop(columns=['is_military'])

        if df_mil.empty:
            print("\nNenhuma aeronave militar detectada no momento.")
            return

        print(f"\nAeronaves militares detectadas: {len(df_mil)}")
        colunas = ['callsign', 'origin_country', 'latitude', 'longitude', 'baro_altitude', 'velocity']
        colunas_existentes = [c for c in colunas if c in df_mil.columns]
        print(df_mil[colunas_existentes].to_string(index=False))
