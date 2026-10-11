from models.piloto import Piloto

def cadastrar_piloto(nome, código, voo_atual, status):
    piloto = Piloto(nome, código, voo_atual, status, [])
    return piloto
