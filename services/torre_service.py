from models.mensagem import mensagem

def cadastrar_mensagem(id, remetente, destinatario, conteudo, horario):
    mensagem = mensagem(id, remetente, destinatario, conteudo, horario, [])
    return mensagem
