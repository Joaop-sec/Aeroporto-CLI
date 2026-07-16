from models.mensagem import mensagem
from API.opensky_service import OpenSkyService

def cadastrar_mensagem(id, remetente, destinatario, conteudo, horario):
    mensagem = mensagem(id, remetente, destinatario, conteudo, horario, [])
    return mensagem

opensky = OpenSkyService()

def monitorar_voos():

    resultado = opensky.buscar_voos()

    if not resultado.success:
        print(resultado.error)
        return

    clima = opensky.buscar_voos()
    print(resultado.data)