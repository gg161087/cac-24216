import os
import sqlite3

DB_NAME = os.path.join(os.path.dirname(__file__), 'inventario.db')

conexion = sqlite3.connect(DB_NAME)

cursor = conexion.cursor()
 
def consulta_categorias():
    consulta = '''SELECT * FROM categorias  '''
    cursor.execute(consulta)
    categorias = cursor.fetchall()
    return categorias

def reporte_productos_por_categoria():
    #consulta a categorias
    categorias = consulta_categorias()
    #listar las categorias
    for categoria in categorias:
        print(categoria)
    #elige la categoria
    cat = int(input("Ingrese categoria"))
   
    consulta = '''SELECT p.descripcion, p.precio, p.cantidad, c.descripcion AS 'Categoría'
                    FROM productos AS p, categorias AS c
                    WHERE p.categoria = c.id_categoria
                    AND c.id_categoria = ?             
                '''
    cursor.execute(consulta, (cat,))
    filas = cursor.fetchall()
    if len(filas) > 0:
        for fila in filas:
            print(fila)
    else:
            print("no hay registros en esa categoria")
    conexion.commit()
    

reporte_productos_por_categoria()
conexion.close()    
