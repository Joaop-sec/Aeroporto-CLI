def exibir_menu_piloto():

    opcao = input("""
=========================================
            ÁREA DO PILOTO
=========================================

1 - Consultar voo atual
2 - Comunicação com a torre
3 - Informações da aeronave

0 - Voltar

=========================================
Escolha uma opção: """)

    return opcao

def consultar_voo_atual():

    opcao = input("""
=========================================
            VOO ATUAL
=========================================

1 - Ver dados do voo
2 - Ver rota planejada
3 - Ver horário de partida
4 - Ver horário de chegada
5 - Ver passageiros embarcados

0 - Voltar

=========================================
Escolha uma opção:
""")

    return opcao

def comunicacao_com_torre():

    opcao = input("""
=========================================
      COMUNICAÇÃO COM A TORRE
=========================================

1 - Enviar mensagem
2 - Receber mensagens
3 - Solicitar autorização de pouso
4 - Solicitar autorização de decolagem
5 - Histórico de comunicações

0 - Voltar

=========================================
Escolha uma opção:
""")

    return opcao

def informacoes_aeronave():

    opcao = input("""
=========================================
      INFORMAÇÕES DA AERONAVE
=========================================

1 - Dados da aeronave
2 - Capacidade de passageiros
3 - Quantidade de combustível
4 - Status de manutenção
5 - Histórico de voos

0 - Voltar

=========================================
Escolha uma opção:
""")

    return opcao