#Equipo 14

#Almacenamiento Inicial de Artistas
artistas = [[1, "The beatles", "Rock"],[2,"Adele", "Pop"]]
next_ID = 3 #ID

def borrar_artista(artistas, artista_id): 
    """
    :params artistas: Lista de artistas[[ID, Nombre, Genero] , ...]
    :params artista_id: ID del artista a borrar.
    :return: True si se elimino correctamente, False en caso contrario.
    """
    for artista in artistas:
        if artista[0] == artista_id:
            artistas.remove(artista)
            print(f"Se elimino el artista {artista[1]} correctamente!.")
            return True #el artista se elimino

    print(f"No se encontro el artista con ID {artista_id}")    
    return False #no se encontro el ID o no se borro

