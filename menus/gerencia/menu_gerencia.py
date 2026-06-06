def exibir_menu_gerencia():

    opcao = input("""
=========================================
          ÁREA DA GERÊNCIA
=========================================

1 - Gerenciar voos
2 - Gerenciar clientes
3 - Gerenciar pilotos
4 - Relatórios

0 - Voltar

=========================================
Escolha uma opção:
""")

    return opcao

def gerenciar_voos():

    opcao = input("""
=========================================
        GERENCIAMENTO DE VOOS
=========================================

1 - Cadastrar voo
2 - Consultar voo
3 - Alterar voo
4 - Cancelar voo
5 - Listar todos os voos

0 - Voltar

=========================================
Escolha uma opção:
""")

    return opcao


def gerenciar_clientes():

    opcao = input("""
=========================================
      GERENCIAMENTO DE CLIENTES
=========================================

1 - Cadastrar cliente
2 - Consultar cliente
3 - Alterar cadastro
4 - Remover cliente
5 - Listar clientes

0 - Voltar

=========================================
Escolha uma opção:
""")

    return opcao


def gerenciar_pilotos():

    opcao = input("""
=========================================
      GERENCIAMENTO DE PILOTOS
=========================================

1 - Cadastrar piloto
2 - Consultar piloto
3 - Alterar piloto
4 - Remover piloto
5 - Listar pilotos

0 - Voltar

=========================================
Escolha uma opção:
""")

    return opcao


def visualizar_relatorios():

    opcao = input("""
=========================================
            RELATÓRIOS
=========================================

1 - Relatório de voos
2 - Relatório de clientes
3 - Relatório de pilotos
4 - Relatório geral do aeroporto

0 - Voltar

=========================================
Escolha uma opção:
""")

    return opcao