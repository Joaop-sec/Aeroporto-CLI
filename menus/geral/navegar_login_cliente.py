from menus.login.menu_login_cliente import exibir_menu_login_cliente
from menus.geral.navegar_cliente import navegar_cliente

def navegar_login_cliente():

    while True:

        opcao = exibir_menu_login_cliente()

        if opcao == '1':
            print("\nFazendo login...")
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu CPF: ")
            senha = input("Digite sua senha: ")

            print(f"\nBem-vindo(a), {nome}!")
            
            navegar_cliente()

        elif opcao == '2':
            print("\nCadastrando novo cliente...")
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu CPF: ")
            senha = input("Digite sua senha: ")

            print(f"\nCliente {nome} cadastrado com sucesso!")

            navegar_cliente()

        elif opcao == '0':
            break

        else:
            print("\nOpção inválida!")







        

