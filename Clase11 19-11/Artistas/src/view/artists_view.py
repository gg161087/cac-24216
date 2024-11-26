def show_artists(artists):
    for artist_id, artist in artists.items():
        print(f"ID: {artist_id}, Nombre: {artist['nombre']}, Género: {artist['género']}, País: {artist['país']}")

def show_artist(artist):
    if artist:
        print(f"Nombre: {artist['nombre']}, Género: {artist['género']}, País: {artist['país']}")
    else:
        print("El artista no fue encontrado.")

def prompt_artist_data():
    nombre = input("Nombre del artista: ")
    género = input("Género del artista: ")
    país = input("País del artista: ")
    return {"nombre": nombre, "género": género, "país": país}

def prompt_artist_id():
    return int(input("ID del artista: "))

def artist_added():
    print("¡Artista agregado exitosamente!")

def artist_updated():
    print("¡Artista actualizado exitosamente!")

def artist_deleted():
    print("¡Artista eliminado exitosamente!")

def artist_not_found():
    print("El artista con ese ID no existe.")
