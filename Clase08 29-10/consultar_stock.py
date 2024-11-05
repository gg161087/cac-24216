# Lista de productos en stock
inventario = ["manzanas", "bananas", "naranjas", "peras", "uvas"]

# Ciclo para consultar productos
while True:
    # Pedimos al usuario que ingrese el nombre del producto a consultar
    producto = input("Ingresa el nombre del producto a consultar (o escribe 'salir' para terminar): ")
    
    # Si el usuario escribe 'salir', finalizamos el programa
    if producto.lower() == 'salir':
        print("Consulta finalizada.")
        break

    # Variable para controlar si encontramos el producto
    encontrado = False
    
    # Bucle while para recorrer la lista de inventario
    i = 0
    while i < len(inventario):
        if inventario[i].lower() == producto.lower():
            encontrado = True
            break
        i += 1

    # Mostramos el resultado de la consulta
    if encontrado:
        print(f"El producto '{producto}' está en stock.")
    else:
        print(f"El producto '{producto}' no está disponible en el inventario.")
