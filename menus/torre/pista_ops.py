from services.pista_service import PistaService
from services.torre_service import verificar_ocupacao_pista

def gerenciar_pistas():
    while True:
        print("\n--- GERENCIAR PISTAS ---")
        print("1 - Listar pistas de um aeroporto")
        print("2 - Verificar ocupação de uma pista")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        if opcao == '1':
            icao = input("Código ICAO do aeroporto (ex: SBGR): ").strip().upper()
            service = PistaService()
            pistas = service.buscar_por_aeroporto(icao)
            if not pistas:
                print("Nenhuma pista encontrada para esse aeroporto.")
            else:
                print(f"\nPistas em {icao}:")
                for p in pistas:
                    print(f"  ID: {p.id} | {p.ident} | {p.length_ft}ft | {p.surface}")

        elif opcao == '2':
            try:
                id_pista = int(input("ID da pista: "))
            except ValueError:
                print("ID inválido.")
                continue
            service = PistaService()
            pista = service.buscar_por_id(id_pista)
            if not pista:
                print("Pista não encontrada.")
                continue

            ocupantes, erro = verificar_ocupacao_pista(pista.le_lat, pista.le_lon)
            if erro:
                print(f"Erro: {erro}")
            elif ocupantes is None:
                print("Não foi possível verificar a ocupação.")
            elif not ocupantes:
                print("Pista livre.")
            else:
                print(f"\nPista ocupada por {len(ocupantes)} aeronave(s):")
                for v in ocupantes:
                    print(f"  {v['callsign']} | dist: {v['dist']:.2f} km | alt: {v['baro_altitude']} m | solo: {v['on_ground']}")

        elif opcao == '0':
            break
        else:
            print("Opção inválida.")