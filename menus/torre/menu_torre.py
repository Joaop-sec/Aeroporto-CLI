from menus.torre.monitoramento import exibir_submenu_monitoramento, exibir_voos_militares
from menus.torre.gerenciar_pistas import gerenciar_pistas

def exibir_menu_torre():
    opcao = input("""
========================
TORRE DE CONTROLE
========================
1 - Monitorar voos
2 - Gerenciar pistas
3 - Rastreio de aeronaves militares
0 - Voltar
========================

Escolha uma opção: """)
    return opcao

def monitorar_voos():
    exibir_submenu_monitoramento()

def rastrear_militares():
    exibir_voos_militares()
    input("\nPressione Enter para continuar.")
