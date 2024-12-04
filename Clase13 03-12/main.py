import os
import sqlite3

DB_NAME = os.path.join(os.path.dirname(__file__), 'personas.db')

def get_connection():
    return sqlite3.connect(DB_NAME)

nuevas_personas = [
    ('Esteban', 32, 'Mar del Plata'),
    ('Valeria', 27, 'Bahía Blanca'),
    ('Fernando', 41, 'Rosario'),
    ('Carolina', 29, 'La Plata'),
    ('Juan', 35, 'Córdoba')
]

def initialize_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age integer NOT NULL,
                city TEXT NOT NULL
            )
        """)
        # conn.commit() Se utiliza cuando utilizamos: INSERT, UPDATE y DELETE
        print('Se creó la tabla "people"')
    except sqlite3.OperationalError: #se usa try except cuando no tiene IF NOT EXISTS el CREATE
        print('La tabla "people" ya existe')
    conn.close()

def create_people(name, age, city):
    query = 'INSERT INTO people (name, age, city) VALUES (?, ?, ?)'
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, (name, age, city))
    conn.commit()
    conn.close()

def create_people_bulk(peaople):
    query = 'INSERT INTO people (name, age, city) VALUES (?, ?, ?)'
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executemany(query, peaople)
    conn.commit()
    conn.close()

# create_people_bulk(nuevas_personas)

if __name__ == "__main__":
    initialize_db()
    #create_people_bulk(nuevas_personas)
    #create_people('Gonzalo', 37, 'La Plata')