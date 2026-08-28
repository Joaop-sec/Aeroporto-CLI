from services.pista_service import PistaService
from services.torre_service import verificar_ocupacao_pista

def exibir_menu_pistas():
    opcao = input("""
=========================================
          GERENCIAMENTO DE PISTAS
=========================================

1 - Ver pistas disponiveis
2 - Reservar pista
3 - Liberar pista
4 - Ver fila de aeronaves
5 - Ver pistas ocupadas
6 - Ver status de uma pista especifica

0 - Voltar

=========================================
Escolha uma opcao: """)
    return opcao

def visualizar_pistas_disponiveis():
    service = PistaService()
    pistas = service.listar_todas(limite=100)
    if not pistas:
        print("\nNenhuma pista cadastrada.")
        return
    print("\n--- PISTAS DISPONIVEIS ---")
    for p in pistas:
        status = "Fechada" if p.closed else "Aberta"
        print(f"  ID: {p.id} | {p.ident} | {p.length_ft}ft | {p.surface} | {status}")

def reservar_pista():
    try:
        id_pista = int(input("ID da pista a reservar: "))
    except ValueError:
        print("ID invalido.")
        return
    service = PistaService()
    pista = service.buscar_por_id(id_pista)
    if not pista:
        print("Pista nao encontrada.")
        return
    print(f"Pista {pista.ident} reservada com sucesso (simulacao).")

def liberar_pista():
    try:
        id_pista = int(input("ID da pista a liberar: "))
    except ValueError:
        print("ID invalido.")
        return
    service = PistaService()
    pista = service.buscar_por_id(id_pista)
    if not pista:
        print("Pista nao encontrada.")
        return
    print(f"Pista {pista.ident} liberada (simulacao).")

def visualizar_fila_aeronaves():
    print("\nFuncionalidade em desenvolvimento...")

def visualizar_pistas_ocupadas():
    service = PistaService()
    pistas = service.listar_todas(limite=50)
    if not pistas:
        print("\nNenhuma pista cadastrada.")
        return
    print("\n--- PISTAS OCUPADAS (DADOS EM TEMPO REAL) ---")
    for p in pistas:
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

def verificar_pista_especifica():
    try:
        id_pista = int(input("Digite o ID da pista: "))
    except ValueError:
        print("ID invalido.")
        return
    service = PistaService()
    pista = service.buscar_por_id(id_pista)
    if not pista:
        print("Pista nao encontrada.")
        return

    print("\n--- DADOS CADASTRAIS DA PISTA ---")
    print(f"ID: {pista.id}")
    print(f"Aeroporto (ICAO): {pista.airport_ident}")
    print(f"Identificacao: {pista.ident}")
    print(f"Comprimento: {pista.length_ft} pes")
    print(f"Largura: {pista.width_ft} pes")
    print(f"Superficie: {pista.surface}")
    print(f"Fechada: {'Sim' if pista.closed else 'Nao'}")
    print(f"Cabeceira 1 - Lat: {pista.le_lat}, Lon: {pista.le_lon}, Rumo: {pista.le_heading}")
    print(f"Cabeceira 2 - Lat: {pista.he_lat}, Lon: {pista.he_lon}, Rumo: {pista.he_heading}")

    ocupantes, erro = verificar_ocupacao_pista(pista.le_lat, pista.le_lon)
    if erro:
        print(f"Erro ao verificar ocupacao: {erro}")
    elif ocupantes is None:
        print("Nao foi possivel verificar a ocupacao.")
    elif not ocupantes:
        print("\nStatus: Pista LIVRE")
    else:
        print(f"\nStatus: Pista OCUPADA por {len(ocupantes)} aeronave(s)")
        for v in ocupantes:
            print(f"  - Callsign: {v['callsign']}, Distancia: {v['dist']:.2f} km, Altitude: {v['baro_altitude']} m, No solo: {v['on_ground']}")

def gerenciar_pistas():
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
        elif opcao == '6':
            verificar_pista_especifica()
        elif opcao == '0':
            break
        else:
            print("\nOpcao invalida.")
        input("\nPressione Enter para continuar...")
