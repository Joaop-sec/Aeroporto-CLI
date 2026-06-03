# =========================================
# IMPORTS - MENU PRINCIPAL
# =========================================

from menus.menu_prinicipal import exibir_menu_principal


# =========================================
# IMPORTS - CLIENTE
# =========================================

from menus.cliente.menu_cliente import exibir_menu_cliente
from menus.cliente.menu_voos import exibir_menu_voos
from menus.cliente.menu_passagens import exibir_menu_passagens
from menus.cliente.menu_historico import exibir_menu_historico
from menus.cliente.menu_cadastro import exibir_menu_cadastro
from menus.cliente.menu_status_voo import exibir_menu_status_voo


# =========================================
# IMPORTS - PILOTO
# =========================================

from menus.piloto.menu_piloto import exibir_menu_piloto
from menus.piloto.menu_voo_atual import exibir_menu_voo_atual
from menus.piloto.menu_comunicacao import exibir_menu_comunicacao as exibir_menu_comunicacao_piloto
from menus.piloto.menu_aeronave import exibir_menu_aeronave


# =========================================
# IMPORTS - TORRE
# =========================================

from menus.torre.menu_torre import exibir_menu_torre
from menus.torre.menu_voos import exibir_menu_voos as exibir_menu_voos_torre
from menus.torre.menu_pistas import exibir_menu_pistas
from menus.torre.menu_comunicacao import exibir_menu_comunicacao as exibir_menu_comunicacao_torre


# =========================================
# ÁREA CLIENTE
# =========================================

def executar_area_cliente():

    while True:

        opcao = exibir_menu_cliente()

        if opcao == '1':
            exibir_menu_voos()

        elif opcao == '2':
            exibir_menu_passagens()

        elif opcao == '3':
            exibir_menu_passagens()

        elif opcao == '4':
            exibir_menu_status_voo()

        elif opcao == '5':
            exibir_menu_historico()

        elif opcao == '6':
            exibir_menu_cadastro()

        elif opcao == '0':
            break

        else:
            print("Opção inválida!")


# =========================================
# ÁREA PILOTO
# =========================================

def executar_area_piloto():

    while True:

        opcao = exibir_menu_piloto()

        if opcao == '1':
            exibir_menu_voo_atual()

        elif opcao == '2':
            exibir_menu_comunicacao_piloto()

        elif opcao == '3':
            exibir_menu_aeronave()

        elif opcao == '0':
            break

        else:
            print("Opção inválida!")


# =========================================
# ÁREA TORRE
# =========================================

def executar_area_torre():

    while True:

        opcao = exibir_menu_torre()

        if opcao == '1':
            exibir_menu_voos_torre()

        elif opcao == '2':
            exibir_menu_pistas()

        elif opcao == '3':
            exibir_menu_comunicacao_torre()

        elif opcao == '0':
            break

        else:
            print("Opção inválida!")


# =========================================
# LOOP PRINCIPAL
# =========================================

while True:

    opcao_principal = exibir_menu_principal()

    if opcao_principal == '1':
        executar_area_cliente()

    elif opcao_principal == '2':
        executar_area_piloto()

    elif opcao_principal == '3':
        executar_area_torre()

    elif opcao_principal == '0':

        print("""
=========================================
       SISTEMA ENCERRADO
=========================================
""")

        break

    else:
        print("Opção inválida!")