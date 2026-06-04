from menus.cliente.menu_cliente import exibir_menu_cliente

def navegar_cliente():

    while True:

        opcao = exibir_menu_cliente()

        if opcao == '1':
            print("Consultar voos")

        elif opcao == '2':
            print("Comprar passagem")

        elif opcao == '0':
            break