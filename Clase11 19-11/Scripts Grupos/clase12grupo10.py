artistas =[
    [1, "The Beatles", "Rock"],
    [2, "Adele", "Pop"]
]
if len(artistas) == 0:
    print("No hay artistas registrados.")
else:
    print("Listado de artistas")
    for artista in artistas:
        print(f"ID: {artista[0]}. Nombre: {artista[1]}. Género: {artista[2]}")
    existe = True
    while existe:
        try:
            id_modificar = int(input("Ingrese el ID del artista a modificar: "))
        except ValueError:
            print("El id debe ser numérico")
        else:
            for artista in artistas:
                if artista[0] == id_modificar:
                    print(artista)
                    nuevo_nombre = input("Ingrese nuevo nombre: ")
                    nuevo_genero = input("Ingrese nuevo genero: ")
                    while not nuevo_nombre:
                        print("Debe ingresar nombre")
                        nuevo_nombre = input("Ingrese nombre del artista: ")
                    while not nuevo_genero:
                        print("Debe ingresar género")
                        nuevo_genero = input("Ingrese genero del artista: ")
                    artista[1] = nuevo_nombre
                    artista[2] = nuevo_genero 
                    print("Artista modificado correctamente")
                    existe = False
                    break 