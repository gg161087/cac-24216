# Almacenamiento inicial
artistas = [[1, “The Beattles”, “Rock”], [2, “Adele”, “Pop”]]
next_id = 3	# ID autoincremental inicial

def agregar_artista(artistas):
    # Solicitar datos
    nombre = ""
    while nombre == "":
        nombre = str(input("Nombre del artista: "))
        if nombre == "":
            print("El campo no puede estar vacío")

    genero = ""
    while genero == "":
        genero = str(input("Género principal: "))
    if genero == "":
        print("El campo no puede estar vacío")


    # Agrega al artista a la lista
    artistas.append((nombre, genero))
    print(f"{nombre} ha sido agregado a la lista.")

agregar_artista(artistas)

Puede ser que vaya esto?
nuevo_artista=[próximo_id, nombre, género]
artistas.append(nuevo_artista)
print(f”El artista {nombre} fue registrado con éxito!”)
próximo_id +1=1


podria ser += próximo_id ? no me acue
claro eso habria que agregarle al final

proximo_id = proximo_id + 1

uh, yo no le agregue que muestre cuando fue registrado, se me paso


# Ingresar el código del artista
 codigo = int(input("Ingrese el código del artista (número entero): "))

 # Verificar si el código ya existe

 if codigo in artistas: print("El código ya está registrado. Intente con otro.") continue