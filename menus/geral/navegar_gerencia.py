from menus.gerencia.menu_gerencia import exibir_menu_gerencia
from menus.gerencia.menu_gerencia import gerenciar_voos
from menus.gerencia.menu_gerencia import gerenciar_clientes
from menus.gerencia.menu_gerencia import gerenciar_pilotos
from menus.gerencia.menu_gerencia import visualizar_relatorios

def navegar_gerencia():

    while True:

        opcao = exibir_menu_gerencia()

        if opcao == '1':
            gerenciar_voos()

        elif opcao == '2':
            gerenciar_clientes()

        elif opcao == '3':
            gerenciar_pilotos()

        elif opcao == '4':
            visualizar_relatorios()

        elif opcao == '0':
            break

        else:
            print("Opção inválida!")
