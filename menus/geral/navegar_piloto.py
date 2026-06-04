from menus.piloto.menu_piloto import exibir_menu_piloto

def navegar_piloto():

    while True:

        opcao = exibir_menu_piloto

        if opcao == '1':
            print("Abrindo menu de voo atual...")

        elif opcao == '2':
            print("Abrindo menu de comunicação...")

        elif opcao == '3':
            print("Abrindo menu de aeronave...")

        elif opcao == '0':
            break

        else:
            print("Opcão invalida")