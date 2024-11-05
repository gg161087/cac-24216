import os
#proyecto integrador
artistas =[
    [1, "The Beatles", "Rock"],
    [2, "Adele", "Pop"]
]

proximo_id = 3 #ID autoincremental

while True:

    print("Menú interactivo")
    print("1. Agregar nuevo artista")
    print("2. Consultar artista")
    print("3. Modificar artista existente")
    print("4. Eliminar artista")
    print("5. Listado completo de artistas")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ").strip()
    if opcion == '1':
        nombre = input("Ingrese nombre del artista")
        genero = input("Ingrese genero del artista")

        while not nombre:
            print("Debe ingresar nombre")
            nombre = input("Ingrese nombre del artista")
        while not genero:
            print("Debe ingresar género")
            genero = input("Ingrese genero del artista")
            
        existe = False
        for artista in artistas:
            if artista[1].lower() == nombre.lower():
                existe = True
                
        if existe:
            print(f"El artista {nombre} ya está registrado")
        else:
            nuevo_artista = [proximo_id, nombre, genero]
            artistas.append(nuevo_artista)
            print(f"El artista {nombre} fue registrado con éxito!")
            proximo_id += 1
    elif opcion == '2':
        #read consulta busqueda
        #search.py
        if len(artistas) == 0:
            print("No hay artistas registrados!")
        else:
            nombre = input("Ingrese nombre del artista a consultar:")
            while not nombre:
                print("Debe ingresar nombre")
                nombre = input("Ingrese nombre del artista")
            
            existe = False
            for artista in artistas:
                if artista[1] == nombre.lower():
                    artista_encontrado = artista
                    existe = True
                    break
            
            if existe == False:
                print("Artista no encontrado!")
            else:
                print(f"ID: {artista_encontrado[0]}")
                print(f"Nombre: {artista_encontrado[1]}")
                print(f"Genero: {artista_encontrado[2]}")
                
    elif opcion == '3':
        #update
        for artista in artistas:
            print(artista)
        
        while True:
            try:
                id_modificar = int(input("Ingrese el ID del artista a modificar:"))
            except ValueError:
                print("El id debe ser numérico")
            else:
                
                for artista in artistas:
                    if artista[0] == id_modificar:
                        print(artista)#mostar la info hallada y preguntar si realmente modifia
                        #if si quiere modifcarlo
                        nuevo_nombre = input("Ingrese nuevo nombre: ")
                        nuevo_genero = input("Ingrese nuevo genero")
                        while not nuevo_nombre:
                            print("Debe ingresar nombre")
                            nuevo_nombre = input("Ingrese nombre del artista")
                        while not nuevo_genero:
                            print("Debe ingresar género")
                            nuevo_genero = input("Ingrese genero del artista")
                        artista[1] = nuevo_nombre
                        artista[2] = nuevo_genero                        
        
    elif opcion == '4':
        #delete
        pass
    elif opcion == '5':
        #read listar
        pass
    elif opcion == '6':
        print("Saliendo del programa....")
        break
    else:
        print("Opcion incorrecta")
