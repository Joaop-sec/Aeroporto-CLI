def exibir_menu_historico():

    opcao = input("""
=========================================
         HISTÓRICO DE VIAGENS
=========================================

1 - Ver todas as viagens
2 - Buscar viagem específica
3 - Estatísticas de viagens

0 - Voltar

=========================================
Escolha uma opção: """)

    return opcao

def visualizar_historico_viagens():

    opcao = input("""
=========================================
         TODAS AS VIAGENS
=========================================

1 - Listar todas as viagens
2 - Ordenar por data
3 - Ordenar por destino

0 - Voltar

=========================================
Escolha uma opção:
""")

    return opcao


def buscar_viagem_historico():

    opcao = input("""
=========================================
       BUSCAR VIAGEM
=========================================

1 - Buscar por código
2 - Buscar por destino
3 - Buscar por data

0 - Voltar

=========================================
Escolha uma opção:
""")

    return opcao


def visualizar_estatisticas_viagens():

    opcao = input("""
=========================================
     ESTATÍSTICAS DE VIAGENS
=========================================

1 - Total de viagens
2 - Destino mais visitado
3 - Quantidade de voos realizados

0 - Voltar

=========================================
Escolha uma opção:
""")

    return opcao