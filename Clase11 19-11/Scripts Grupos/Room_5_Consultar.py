artistas = [[1, "the Beatles", "rock"], [2, "adele", "pop"]]


def buscador_artista(artistas, nombre_artista):
    for artista in artistas:
        if artista[1].lower() == nombre_artista.lower():
            return artista
    return []

def buscar_artista():
    while True:
        nombre_a_buscar = input("Ingrese el nombre del artista: ")

        resultado = buscador_artista(artistas, nombre_a_buscar)

        if resultado:
            print(f"ID: {resultado[0]}")
            print(f"Artista encontrado: {resultado[1]}")
            print(f"Género: {resultado[2]}")
            break
        else:
            print("Artista no encontrado.")

buscar_artista()