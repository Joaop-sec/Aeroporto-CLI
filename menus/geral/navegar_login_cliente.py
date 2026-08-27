from menus.login.menu_login_cliente import exibir_menu_login_cliente
from services.client_service import cadastrar_cliente, realizar_login_cliente
from menus.geral.navegar_cliente import navegar_cliente

# GUI
from GUI.gui_login import executar_janela_login







def navegar_login_cliente():

    while True:

        opcao = exibir_menu_login_cliente()

        if opcao == '1':
            print("\nFazendo login...")
            cpf = input("Digite seu CPF: ")
            
            cliente = realizar_login_cliente(cpf)

            
            
            if cliente:
                print(f"\nBem-vindo(a), {cliente['nome']}!")
                navegar_cliente()
            else:
                print("\nCPF não encontrado. Tente novamente.")


        elif opcao == '2':
            executar_janela_login()

 
        elif opcao == '0':
            break

        else:
            print("\nOpção inválida!")






        

