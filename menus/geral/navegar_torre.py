from menus.torre.menu_torre import exibir_menu_torre
from menus.torre.menu_torre import monitorar_voos
from menus.torre.menu_torre import gerenciar_pistas
from menus.torre.menu_torre import comunicacao_com_pilotos

def navegar_torre():

    while True:

        opcao = exibir_menu_torre()

        if opcao == '1':
            monitorar_voos()

        elif opcao == '2':
            gerenciar_pistas()

        elif opcao == '3':
            comunicacao_com_pilotos()

        elif opcao == '0':
            break

        else:
            print("Opção inválida!")