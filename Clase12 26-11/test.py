import os
import sqlite3

DB_NAME = os.path.join(os.path.dirname(__file__), "artists.db")
conn = sqlite3.connect(DB_NAME)

# Crear el cursor para ejecutar consultas
cursor = conn.cursor()

def read_artists():
    cursor.execute("SELECT * FROM Artist;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

read_artists()