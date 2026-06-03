from models.cliente import Cliente

def cadastrar_cliente(nome, cpf, id_cliente):
    cliente = Cliente(nome, cpf, id_cliente, [])
    return cliente


