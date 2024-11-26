
id=2
artistas = {
    1: {"nombre":"The Beatles", "Genero": "Rock"},
    2: {"nombre": "Adele", "Genero": "Pop"},
}


while respuesta == "s":

    nombre = input("Ingrese nombre del artista:\t")
    genero = input("Ingrese género del artista:\t")
    respuesta = input("Desea seguir ingresando artistas (s\n):\t")
    id += 1

artista  = {"nombre": nombre, "genero": genero}


artistas [id] = artista


print(artistas)

