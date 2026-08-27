import os
import sqlite3

# 1. MODELO DA ENTIDADE 
class Piloto:
    def __init__(self, codigo, nome, status, aeronave, horario_voo):
        self.codigo = codigo
        self.nome = nome
        self.status = status
        self.aeronave = aeronave
        self.horario_voo = horario_voo


# 2. GERENCIADOR DO BANCO DE DADOS 
class BancoDados:
    def __init__(self, nome_banco="banco_pilotos.bd"):
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        self.nome_banco = os.path.join(pasta_atual, nome_banco)
        self.conectar_e_criar_tabela()

    def conectar_e_criar_tabela(self):
        """Cria a conexão e a tabela de piloto se ela não existir"""
        connection = sqlite3.connect(self.nome_banco)
        cursor = connection.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS piloto(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                codigo TEXT NOT NULL,
                nome TEXT NOT NULL,
                status TEXT NOT NULL,
                aeronave TEXT NOT NULL,
                horario_voo TEXT NOT NULL
            )
        """)
        
        connection.commit()
        connection.close()

    def inserir_piloto(self, piloto: Piloto):
        """Recebe um objeto da classe Piloto e insere no banco de dados"""
        connection = sqlite3.connect(self.nome_banco)
        cursor = connection.cursor()
        
        sql = """
            INSERT INTO piloto (codigo, nome, status, aeronave, horario_voo)
            VALUES (?, ?, ?, ?, ?)
        """
        
        valores = (
            piloto.codigo, 
            piloto.nome, 
            piloto.status, 
            piloto.aeronave, 
            piloto.horario_voo, 
        )
        
        cursor.execute(sql, valores)
        connection.commit()
        connection.close()
        print(f"\n[Sucesso] Piloto {piloto.nome} salvo no banco de dados!")


# 3. BLOCO DE EXECUÇÃO INTERATIVO 
if __name__ == "__main__":
    db = BancoDados()
    
    print("=" * 40)
    print("  SISTEMA DE TRÁFEGO AÉREO: CADASTRO_PILOTO  ")
    print("=" * 40)
    
    nome_piloto = input("Digite o nome do piloto: ")
    codigo_piloto = input("Digite o codigo do piloto: ")
    status_piloto = input("Digite o status do piloto: ")
    status_aeronave = input("Digite a aeronave: ")
    h_voo = input("Digite o horário do voo: ")
    
    novo_piloto = Piloto(
        codigo=codigo_piloto,
        nome=nome_piloto,
        status=status_piloto,
        aeronave=status_aeronave,
        horario_voo=h_voo
    )
    
    db.inserir_piloto(novo_piloto)
    print("=" * 40)