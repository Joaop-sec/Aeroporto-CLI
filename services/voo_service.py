from models.voo import voo

def cadastrar_voo(código_de_voo, origem, destino, horario, piloto_responsavel, copiloto_responsavel, status):
    voo = voo(código_de_voo, origem, destino, horario, piloto_responsavel, copiloto_responsavel, status)
    return voo