import sqlite3

# 1. MODELO DA ENTIDADE 
class Cliente:
    def __init__(self, cpf, numero_passaporte, pais_emissor, nome_completo, data_nascimento, nacionalidade):
        self.cpf = cpf
        self.numero_passaporte = numero_passaporte
        self.pais_emissor = pais_emissor
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.nacionalidade = nacionalidade


# 2. GERENCIADOR DO BANCO DE DADOS 
class BancoDados:
    def __init__(self, nome_banco=None):
        import os
        # Descobre a pasta exata onde o arquivo bank.py está salvo
        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        self.nome_banco = os.path.join(pasta_atual, "bank.bd")
        self.conectar_e_criar_tabela()


    def conectar_e_criar_tabela(self):
        """Cria a conexão e a tabela de clientes se ela não existir"""
        connection = sqlite3.connect(self.nome_banco)
        cursor = connection.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                cpf TEXT NOT NULL,
                numero_passaporte TEXT NOT NULL,
                pais_emissor TEXT NOT NULL,
                nome_completo TEXT NOT NULL,
                data_nascimento TEXT NOT NULL,
                nacionalidade TEXT NOT NULL
            )
        """)
        
        connection.commit()
        connection.close()

    def inserir_cliente(self, cliente: Cliente):
        """Recebe um objeto da classe Cliente e insere no banco de dados"""
        connection = sqlite3.connect(self.nome_banco)
        cursor = connection.cursor()
        
  
        sql = """
            INSERT INTO clientes (cpf, numero_passaporte, pais_emissor, nome_completo, data_nascimento, nacionalidade)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        
        valores = (
            cliente.cpf, 
            cliente.numero_passaporte, 
            cliente.pais_emissor, 
            cliente.nome_completo, 
            cliente.data_nascimento, 
            cliente.nacionalidade
        )
        
        cursor.execute(sql, valores)
        connection.commit()
        connection.close()
        print(f"\n[Sucesso] Cliente {cliente.nome_completo} salvo no banco de dados!")


# 3. BLOCO DE EXECUÇÃO INTERATIVO 
if __name__ == "__main__":
    # Inicializa o banco 
    db = BancoDados()
    
    print("=" * 40)
    print("  SISTEMA DE TRÁFEGO AÉREO: CADASTRO  ")
    print("=" * 40)
    
    # Captura as informações digitadas pelo usuário
    nome = input("Digite o nome completo: ")
    cpf_cliente = input("Digite o CPF: ")
    passaporte = input("Digite o número do passaporte: ")
    pais = input("Digite o país emissor do passaporte: ")
    nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    nacio = input("Digite a nacionalidade: ")
    
    # Transforma as strings digitadas em um Objeto da classe Cliente
    novo_cliente = Cliente(
        cpf=cpf_cliente,
        numero_passaporte=passaporte,
        pais_emissor=pais,
        nome_completo=nome,
        data_nascimento=nascimento,
        nacionalidade=nacio
    )
    
    # Envia o objeto para o método que faz o INSERT
    db.inserir_cliente(novo_cliente)
    print("=" * 40)