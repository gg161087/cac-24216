#1.Registro Artistas
#2.Consulta artistas
#3.Reporte artistas registrados
#4.actualizar artista
#5.Borrar artista

#Almacenamiento inicial
artistas = [ [1, "the beatles","Rock"], [2, "Adele", "Pop"] ]

next_id = 3 #ID Autoincremental

# Convertir a diccionario
artistas_dict = {artista[0]: {"nombre": artista[1], "genero": artista[2]} for artista in artistas}

# Mostrar el diccionario
print(artistas_dict)

def actualizar_artista(artistas_dict, id_artista, nuevo_nombre=None, nuevo_genero=None):
    if id_artista in artistas_dict:
        if nuevo_nombre:
            artistas_dict[id_artista]["nombre"] = nuevo_nombre
        if nuevo_genero:
            artistas_dict[id_artista]["genero"] = nuevo_genero
        print(f"Artista actualizado: {artistas_dict[id_artista]}")
    else:
        print(f"No se encontró ningún artista con ID {id_artista}.")

# Ejemplo de uso
actualizar_artista(artistas_dict, 1, nuevo_nombre="The Beatles", nuevo_genero="Rock Clásico")
print(artistas_dict)