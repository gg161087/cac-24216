# Diccionario para almacenar los artistas registrados
artistas = {
    "Artista1": {"genero": "Pop"},
    "Artista2": {"genero": "Rock"}
}

def actualizar_artista(artistas):
    # Solicita el nombre del artista a actualizar
    nombre = input("Ingrese el nombre del artista a actualizar: ")
    if nombre in artistas:
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nuevo_genero = input("Ingrese el nuevo género: ")
        # Actualiza el artista en el diccionario
        artistas[nuevo_nombre] = {'genero': nuevo_genero}
        if nuevo_nombre != nombre:
            del artistas[nombre]  # Elimina el antiguo nombre si se cambió
        print("Artista actualizado con éxito.")
    else:
        print("Artista no encontrado.")

def menu():
    # Muestra el menú y gestiona las opciones
    while True:
        print("\n1. Registrar Artista")
        print("2. Consultar Artista")
        print("3. Reporte de Artistas")
        print("4. Actualizar Artista")
        print("5. Borrar Artista")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '4':
            actualizar_artista(artistas)  # Pasar el diccionario a la función
        elif opcion == '6':
            break  # Salir del menú
        else:
            print("Opción no válida.")

# Ejecutar menú
menu()