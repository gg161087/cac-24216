import sqlite3 
from src.data.db_connection import get_connection

def insert_persona(nombre, edad, ciudad):
    query = f"""
        INSERT INTO Personas (nombre, edad, ciudad) VALUES (?, ?, ?)
    """    
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query, (nombre, edad, ciudad))
        conn.commit()                    
        return True
    except sqlite3.IntegrityError as e:
        print(f'Error: {e}')
        return None
    finally:
        if conn:  # Verifica si `conn` fue inicializado
            conn.close()

def fetch_all_personas():
    query = f'SELECT * FROM Personas'   
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        keys = ['id', 'nombre', 'edad', 'ciudad']
        dict_results = [dict(zip(keys, row)) for row in results]
        return dict_results
    except sqlite3.Error as e:  # Manejar errores de SQLite
        print(f'Error al obtener los productos: {e}')
        return None
    finally:
        if conn:  # Verifica si `conn` fue inicializado
            conn.close()   

def fetch_persona_dynamic(condition, parameter):
    query = f'SELECT * FROM Personas WHERE {condition} = ?'
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query, (parameter,))    
        row = cursor.fetchone()
        conn.close()    
        if row:        
            return {
                "id": row[0],
                "nombre": row[1],
                "edad": row[2],
                "ciudad": row[3]
            }
    except sqlite3.Error as e:  # Manejar errores de SQLite
        print(f'Error al obtener el producto: {e}')
        return None    
    finally:
        if conn:  # Verifica si `conn` fue inicializado
            conn.close()

def update_persona_by_id(id, nombre, edad, ciudad):
    query = """
        UPDATE Personas
        SET nombre = ?, edad = ?, ciudad = ?
        WHERE id = ?
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query, (nombre, edad, ciudad, id))
        conn.commit()
        updated_rows = cursor.rowcount
        conn.close()
        return updated_rows > 0
    except sqlite3.Error as e:  # Manejar errores de SQLite
        print(f'Error al actualizar la persona con ID {id}: {e}')
        return False  # Devuelve `False` en caso de error
    finally:
        if 'conn' in locals():  # Verifica si `conn` fue inicializado
            conn.close()   

def delete_persona_by_id(id):
    query_check = 'SELECT 1 FROM Personas WHERE id = ?'
    query_delete = 'DELETE FROM Personas WHERE id = ?'
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Verificar si el producto existe
        cursor.execute(query_check, (id,))
        product_exists = cursor.fetchone()
        if product_exists:
            # El producto existe, proceder con la eliminación
            cursor.execute(query_delete, (id,))
            conn.commit()
            return True  # Indica que se eliminó exitosamente
        else:
            # El producto no existe
            return False  # Indica que no se encontró el producto
    except sqlite3.Error as e:
        print(f'Error al intentar eliminar la persona con ID {id}: {e}')
        return False
    finally:
        if 'conn' in locals():  # Asegura que la conexión se cierre si fue creada
            conn.close()
    