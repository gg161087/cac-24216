# Grupo 7 - Tarea 3 
#3.Reporte artistas registrados

#Almacenamiento inicial
artistas = [ [1, "the beatles","Rock"], [2, "Adele", "Pop"] ]

next_id = 3 #ID Autoincremental

def mostrar_artistas():
    if not artistas:
        print("No hay artistas registrados.")
    else:
        for artista in artistas:
            id_artista = artista[0]
            nombre = artista[1]
            genero = artista[2]
            print(f"ID: {id_artista}, Nombre: {nombre}, Género: {genero}")

mostrar_artistas()
