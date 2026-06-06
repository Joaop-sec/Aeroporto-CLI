from menus.piloto.menu_piloto import exibir_menu_piloto
from menus.piloto.menu_piloto import consultar_voo_atual
from menus.piloto.menu_piloto import comunicacao_com_torre
from menus.piloto.menu_piloto import informacoes_aeronave

def navegar_piloto():

    while True:

        opcao = exibir_menu_piloto()

        if opcao == '1':
            consultar_voo_atual()

        elif opcao == '2':
            comunicacao_com_torre()

        elif opcao == '3':
            informacoes_aeronave()

        elif opcao == '0':
            break

        else:
            print("Opcão invalida")