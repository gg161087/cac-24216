artistas = {
    1: {"nombre": "Taylor Swift", "genero": "Pop", "pais": "Estados Unidos"},
    2: {"nombre": "Shakira", "genero": "Pop", "pais": "Colombia"},
    3: {"nombre": "Bad Bunny", "genero": "Regueton", "país": "Puerto Rico"},
    4: {"nombre": "Adele", "genero": "Soul", "pais": "Reino Unido"},
    5: {"nombre": "Rosalía", "genero": "Flamenco", "pais": "España"},
}

clave = int(input("Ingresa el cdigo del artista: "))
paso=0

for codigo, datos in artistas.items():

    if clave==codigo:
        print(f"Artista encontrado: {artistas[clave]}")
        paso=1    
        nuevo_nombre = input("Ingresa el nuevo nombre del artista (deja en blanco para no modificar): ")
        nuevo_genero = input("Ingresa el nuevo genero del artista (deja en blanco para no modificar): ")
        nuevo_pais = input("Ingresa el nuevo pais del artista (deja en blanco para no modificar): ")
   
        if nuevo_nombre:
            artistas[clave]["nombre"] = nuevo_nombre
        if nuevo_genero:
            artistas[clave]["genero"] = nuevo_genero
        if nuevo_pais:
            artistas[clave]["pais"] = nuevo_pais   
        print("Artista actualizado")


if paso==0:
    print ("no se encontro!")

print("Lista actualizada:")
for codigo, datos in artistas.items():
    print(f"{codigo}: {datos}")