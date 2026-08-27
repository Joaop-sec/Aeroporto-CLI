from models.piloto import Piloto
from utils.persistencia import (salvar_pilotos, carregar_pilotos)

def cadastrar_piloto(nome, senha, código, voo_atual, status):
    piloto = {"nome": nome, "senha": senha, "código": código, "voo_atual": voo_atual, "status": status}

    pilotos = carregar_pilotos()

    pilotos.append(piloto)

    salvar_pilotos(pilotos)

    return piloto

def realizar_login_piloto(senha):

    pilotos = carregar_pilotos()

    for piloto in pilotos:
        if piloto["senha"] == senha:
            return piloto
        
    return None