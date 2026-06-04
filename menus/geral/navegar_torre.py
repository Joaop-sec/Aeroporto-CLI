from menus.torre.menu_torre import exibir_menu_torre

def navegar_torre():

    while True:

        opcao = exibir_menu_torre()

        if opcao == '1':
            print("Abrindo menu de voos...")

        elif opcao == '2':
            print("Abrindo menu de pistas...")

        elif opcao == '3':
            print("Abrindo menu de comunicação...")

        elif opcao == '0':
            break

        else:
            print("Opção inválida!")