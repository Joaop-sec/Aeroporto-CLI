from menus.gerencia.menu_gerencia import exibir_menu_gerencia

def navegar_gerencia():

    while True:

        opcao = exibir_menu_gerencia()

        if opcao == '1':
            print("Abrindo gerenciamento de voos...")

        elif opcao == '2':
            print("Abrindo gerenciamento de clientes...")

        elif opcao == '3':
            print("Abrindo gerenciamento de pilotos...")

        elif opcao == '4':
            print("Abrindo relatórios...")

        elif opcao == '0':
            break

        else:
            print("Opção inválida!")