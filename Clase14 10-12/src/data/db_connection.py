import os
import sqlite3

base_de_datos = os.path.join(os.path.dirname(__file__), 'base_de_datos.db')

def get_connection():
    return sqlite3.connect(base_de_datos)

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            edad INTEGER,
            ciudad TEXT
        )
    """
    )
    conn.commit()
    conn.close()