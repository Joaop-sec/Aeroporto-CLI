from menus.piloto.menu_piloto import exibir_menu_piloto
from menus.piloto.menu_voo_atual import consultar_voo_atual
from menus.piloto.menu_comunicacao import exibir_menu_comunicacao
from menus.piloto.menu_aeronave import consultar_informacoes_aeronave

def navegar_piloto():

    while True:

        opcao = exibir_menu_piloto()

        if opcao == '1':
            consultar_voo_atual()

        elif opcao == '2':
            exibir_menu_comunicacao()

        elif opcao == '3':
            consultar_informacoes_aeronave()

        elif opcao == '0':
            break

        else:
            print("Opcão invalida")