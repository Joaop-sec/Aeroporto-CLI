import json


def carregar_clientes():

    try:

        with open("/home/joaopedro/Downloads/Projetos - Python/Aeroporto CLI/data/clientes.json", "r", encoding="utf-8") as arquivo:

            return json.load(arquivo)

    except FileNotFoundError:

        return []


def salvar_clientes(clientes):

        with open("/home/joaopedro/Downloads/Projetos - Python/Aeroporto CLI/data/clientes.json", "w", encoding="utf-8") as arquivo:

            json.dump(clientes, arquivo, indent=4, ensure_ascii=False)



def carregar_pilotos():

    try:

        with open("/home/joaopedro/Downloads/Projetos - Python/Aeroporto CLI/data/pilotos.json", "r", encoding="utf-8") as arquivo:

            return json.load(arquivo)

    except FileNotFoundError:

        return []

def salvar_pilotos(pilotos):

        with open("/home/joaopedro/Downloads/Projetos - Python/Aeroporto CLI/data/pilotos.json", "w", encoding="utf-8") as arquivo:

            json.dump(pilotos, arquivo, indent=4, ensure_ascii=False)

