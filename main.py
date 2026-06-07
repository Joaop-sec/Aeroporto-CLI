from menus.geral.menu_prinicipal import exibir_menu_principal

from menus.geral.navegar_login_cliente import navegar_login_cliente
from menus.geral.navegar_login_piloto import navegar_login_piloto
from menus.geral.navegar_torre import navegar_torre
from menus.geral.navegar_gerencia import navegar_gerencia

while True:

    opcao = exibir_menu_principal()

    if opcao == '1':
        navegar_login_cliente()

    elif opcao == '2':
        navegar_login_piloto()

    elif opcao == '3':
        navegar_torre()

    elif opcao == '4':
        navegar_gerencia()

    elif opcao == '0':
        print("\nEncerrando sistema...")
        break

    else:
        print("\nOpcão inválida")


