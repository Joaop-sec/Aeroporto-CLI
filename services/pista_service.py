import sqlite3
from models.pista import Pista

class PistaService:
    def __init__(self, db_path="data/bank.bd"):
        self.db_path = db_path

    def _conectar(self):
        return sqlite3.connect(self.db_path)

    def listar_todas(self, limite=100):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pistas LIMIT ?", (limite,))
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_pista(row) for row in rows]

    def buscar_por_aeroporto(self, icao):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pistas WHERE airport_ident = ?", (icao.upper(),))
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_pista(row) for row in rows]

    def buscar_por_id(self, id_pista):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pistas WHERE id = ?", (id_pista,))
        row = cursor.fetchone()
        conn.close()
        return self._row_to_pista(row) if row else None

    def _row_to_pista(self, row):
        return Pista(
            id=row[0],
            airport_ident=row[1],
            ident=row[2],
            length_ft=row[3],
            width_ft=row[4],
            surface=row[5],
            closed=row[6],
            le_lat=row[7],
            le_lon=row[8],
            le_heading=row[9],
            he_lat=row[10],
            he_lon=row[11],
            he_heading=row[12]
        )
