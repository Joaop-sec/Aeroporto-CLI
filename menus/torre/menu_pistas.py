from services.pista_service import PistaService
from services.torre_service import verificar_ocupacao_pista

def exibir_menu_pistas():
    opcao = input("""
=========================================
          GERENCIAMENTO DE PISTAS
=========================================

1 - Ver pistas disponíveis
2 - Reservar pista
3 - Liberar pista
4 - Ver fila de aeronaves
5 - Ver pistas ocupadas

0 - Voltar

=========================================
Escolha uma opção: """)
    return opcao

def visualizar_pistas_disponiveis():
    """Lista todas as pistas cadastradas (limitado a 100 para não sobrecarregar)."""
    service = PistaService()
    pistas = service.listar_todas(limite=100)
    if not pistas:
        print("\nNenhuma pista cadastrada.")
        return
    print("\n--- PISTAS DISPONÍVEIS ---")
    for p in pistas:
        status = "Fechada" if p.closed else "Aberta"
        print(f"  ID: {p.id} | {p.ident} | {p.length_ft}ft | {p.surface} | {status}")

def reservar_pista():
    """Reserva uma pista (muda status para ocupada)."""
    try:
        id_pista = int(input("ID da pista a reservar: "))
    except ValueError:
        print("ID inválido.")
        return
    service = PistaService()
    pista = service.buscar_por_id(id_pista)
    if not pista:
        print("Pista não encontrada.")
        return

    print(f"Pista {pista.ident} reservada com sucesso (simulação).")

def liberar_pista():
    """Libera uma pista (muda status para livre)."""
    try:
        id_pista = int(input("ID da pista a liberar: "))
    except ValueError:
        print("ID inválido.")
        return
    service = PistaService()
    pista = service.buscar_por_id(id_pista)
    if not pista:
        print("Pista não encontrada.")
        return
    print(f"Pista {pista.ident} liberada (simulação).")

def visualizar_fila_aeronaves():
    """Exibe uma fila simulada de aeronaves aguardando (futuro)."""
    print("\nFuncionalidade em desenvolvimento...")

def visualizar_pistas_ocupadas():
    """Verifica, usando a OpenSky, quais pistas estão ocupadas no momento."""
    service = PistaService()
    pistas = service.listar_todas(limite=50)  # limite para não sobrecarregar
    if not pistas:
        print("\nNenhuma pista cadastrada.")
        return
    print("\n--- PISTAS OCUPADAS (DADOS EM TEMPO REAL) ---")
    for p in pistas:
        # Usa a cabeceira 1 como referência
        ocupantes, erro = verificar_ocupacao_pista(p.le_lat, p.le_lon)
        if erro:
            print(f"  Pista {p.ident}: erro ao verificar - {erro}")
        elif ocupantes is None:
            print(f"  Pista {p.ident}: sem dados")
        elif not ocupantes:
            print(f"  Pista {p.ident}: livre")
        else:
            print(f"  Pista {p.ident}: ocupada por {len(ocupantes)} aeronave(s)")
            for v in ocupantes:
                print(f"    - {v['callsign']} a {v['dist']:.2f} km, alt {v['baro_altitude']} m")

def gerenciar_pistas():
    """Função principal que controla o loop do menu de pistas."""
    while True:
        opcao = exibir_menu_pistas()
        if opcao == '1':
            visualizar_pistas_disponiveis()
        elif opcao == '2':
            reservar_pista()
        elif opcao == '3':
            liberar_pista()
        elif opcao == '4':
            visualizar_fila_aeronaves()
        elif opcao == '5':
            visualizar_pistas_ocupadas()
        elif opcao == '0':
            break
        else:
            print("\nOpção inválida.")
        input("\nPressione Enter para continuar...")