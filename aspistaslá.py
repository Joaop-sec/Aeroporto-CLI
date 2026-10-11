import pandas as pd
import sqlite3
import urllib.request

url = "https://davidmegginson.github.io/ourairports-data/runways.csv"
urllib.request.urlretrieve(url, "runways.csv")

df = pd.read_csv("runways.csv")

conn = sqlite3.connect("data/bank.bd")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pistas (
    id INTEGER PRIMARY KEY,
    airport_ident TEXT,
    ident TEXT,
    length_ft REAL,
    width_ft REAL,
    surface TEXT,
    closed INTEGER,
    le_lat REAL,
    le_lon REAL,
    le_heading REAL,
    he_lat REAL,
    he_lon REAL,
    he_heading REAL
)
""")

# Inserir dados (apenas pistas com coordenadas válidas)
for _, row in df.iterrows():
    if pd.isna(row['le_latitude_deg']) or pd.isna(row['le_longitude_deg']):
        continue
    cursor.execute("""
    INSERT OR REPLACE INTO pistas (
        id, airport_ident, ident, length_ft, width_ft, surface, closed,
        le_lat, le_lon, le_heading, he_lat, he_lon, he_heading
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        row['id'],
        row['airport_ident'],
        f"{row['le_ident']}/{row['he_ident']}" if pd.notna(row['le_ident']) and pd.notna(row['he_ident']) else None,
        row['length_ft'],
        row['width_ft'],
        row['surface'],
        row['closed'],
        row['le_latitude_deg'],
        row['le_longitude_deg'],
        row['le_heading_degT'],
        row['he_latitude_deg'],
        row['he_longitude_deg'],
        row['he_heading_degT']
    ))

conn.commit()
conn.close()
print("Importação concluída.")