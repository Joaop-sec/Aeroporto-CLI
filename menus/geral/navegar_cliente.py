from menus.cliente.menu_cliente import exibir_menu_cliente
from menus.cliente.menu_cliente import consultar_voos_disponiveis
from menus.cliente.menu_cliente import comprar_passagem
from menus.cliente.menu_cliente import visualizar_minhas_passagens
from menus.cliente.menu_cliente import consultar_status_voo
from menus.cliente.menu_cliente import visualizar_historico_viagens
from menus.cliente.menu_cliente import atualizar_cadastro_cliente

def navegar_cliente():

    while True:

        opcao = exibir_menu_cliente()

        if opcao == '1':
            consultar_voos_disponiveis()
            

        elif opcao == '2':
            comprar_passagem()
        
        elif opcao == '3':
            visualizar_minhas_passagens()

        elif opcao == '4':
            consultar_status_voo()

        elif opcao == '5':
            visualizar_historico_viagens()

        elif opcao == '6':
            atualizar_cadastro_cliente()

        elif opcao == '0':
            break