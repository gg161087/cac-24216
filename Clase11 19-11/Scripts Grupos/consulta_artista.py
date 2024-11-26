artistas = {
    1: {"nombre": "taylor swift", "genero": "pop", "pais": "estados unidos"},
    2: {"nombre": "shakira", "genero": "pop", "pais": "colombia"},
    3: {"nombre": "bad bunny", "genero": "reagueton", "pais": "puerto rico"},
    4: {"nombre": "adele", "genero": "soul", "pais": "reino unido"},
    5: {"nombre": "rosalia", "genero": "flamenco", "pais": "españa"}
}

def consultar_artista():
    print("\n--- Consultar Artista ---")
    print("1. Buscar por ID")
    print("2. Buscar por Nombre")
    print("3. Buscar por Género")
    print("4. Buscar por País")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":  
        id_buscar = int(input("Ingrese el ID del artista a consultar: "))
        if id_buscar in artistas:
            datos = artistas[id_buscar]
            print(f"ID: {id_buscar}, Nombre: {datos['nombre']}, Género: {datos['genero']}, País: {datos['pais']}")
        else:
            print("Artista no encontrado.")
    
    elif opcion == "2":  
        nombre_buscar = input("Ingrese el nombre del artista a consultar: ").lower()
        encontrados = [id for id, datos in artistas.items() if datos["nombre"].lower() == nombre_buscar]
        if encontrados:
            print("Artistas encontrados:")
            for id in encontrados:
                datos = artistas[id]
                print(f"ID: {id}, Nombre: {datos['nombre']}, Género: {datos['genero']}, País: {datos['pais']}")
        else:
            print("No se encontraron artistas con ese nombre.")
    
    elif opcion == "3":  
        genero_buscar = input("Ingrese el género musical a consultar: ").lower()
        encontrados = [id for id, datos in artistas.items() if datos["genero"].lower() == genero_buscar]
        if encontrados:
            print("Artistas encontrados:")
            for id in encontrados:
                datos = artistas[id]
                print(f"ID: {id}, Nombre: {datos['nombre']}, Género: {datos['genero']}, País: {datos['pais']}")
        else:
            print("No se encontraron artistas en ese género.")
    
    elif opcion == "4":  
        pais_buscar = input("Ingrese el país del artista a consultar: ").lower()
        encontrados = [id for id, datos in artistas.items() if datos["pais"].lower() == pais_buscar]
        if encontrados:
            print("Artistas encontrados:")
            for id in encontrados:
                datos = artistas[id]
                print(f"ID: {id}, Nombre: {datos['nombre']}, Género: {datos['genero']}, País: {datos['pais']}")
        else:
            print("No se encontraron artistas de ese país.")
    
    else:
        print("Opción inválida. Intente nuevamente.")