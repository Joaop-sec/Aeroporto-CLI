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