from menus.login.menu_login_piloto import exibir_menu_login_piloto
from menus.geral.navegar_piloto import navegar_piloto

def navegar_login_piloto():

    while True:

        opcao = exibir_menu_login_piloto()

        if opcao == '1':
            print("\nFazendo login...")
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu CPF: ")
            senha = input("Digite sua senha: ")

            print(f"\nBem-vindo(a), {nome}!")
            
            navegar_piloto()

        elif opcao == '2':
            print("\nCadastrando novo piloto...")
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu CPF: ")
            senha = input("Digite sua senha: ")

            print(f"\nPiloto {nome} cadastrado com sucesso!")

            navegar_piloto()

        elif opcao == '0':
            break

        else:
            print("\nOpção inválida!")





from menus.login.menu_login_cliente import exibir_menu_login_cliente

from services.client_service import cadastrar_cliente, realizar_login_cliente

from menus.geral.navegar_cliente import navegar_cliente

def navegar_login_cliente():

    while True:

        opcao = exibir_menu_login_cliente()

        if opcao == '1':
            print("\nFazendo login...")
            cpf = input("Digite seu CPF: ")
            
            cliente = realizar_login_cliente(cpf)

            
            
            if cliente:
                print(f"\nBem-vindo(a), {cliente['nome']}!")
                navegar_cliente()
            else:
                print("\nCPF não encontrado. Tente novamente.")

        elif opcao == '2':
            print("\nCadastrando novo cliente...")
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu CPF: ")

            cadastrar_cliente(nome, cpf)

            print(f"\nCliente {nome} cadastrado com sucesso!")

            

        elif opcao == '0':
            break

        else:
            print("\nOpção inválida!")
