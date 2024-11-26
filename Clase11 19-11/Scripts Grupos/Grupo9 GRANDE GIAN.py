# Almacenamiento inicial de artistas
artistas = {
    1: {"nombre": "The Beatles", "genero": "Rock"},
    2: {"nombre": "Adele", "genero": "Pop"}
}
next_id = 3  # ID autoincremental inicial

def mostrar_artistas():
    if not artistas:
        print("No hay artistas registrados.")
    else:
        print("Artistas registrados:")
        for id_artista, datos in artistas.items():
            print(f"ID: {id_artista}, Nombre: {datos['nombre']}, Género: {datos['genero']}")


    while True:
        print("\nSistema de Gestión de Artistas")
        print("1. Mostrar artistas registrados")
        print("2. Salir")
        
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            mostrar_artistas()
        elif opcion == "2":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

