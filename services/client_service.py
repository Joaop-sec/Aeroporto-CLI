from models.cliente import Cliente
from utils.persistencia import (salvar_clientes, carregar_clientes)

def cadastrar_cliente(nome, cpf):
    cliente = {"nome": nome, "cpf": cpf}
    
    clientes = carregar_clientes()
    
    clientes.append(cliente)

    salvar_clientes(clientes)

    return cliente


def realizar_login_cliente(cpf):

    clientes = carregar_clientes()

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
        
    return None
      