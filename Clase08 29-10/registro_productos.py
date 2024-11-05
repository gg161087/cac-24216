# Inicializamos la lista vacía para almacenar los productos
inventario = []

# Usamos un bucle para permitir que el usuario agregue productos
while True:
    # Pedimos el nombre del producto al usuario
    producto = input("Ingresa el nombre del producto (o escribe 'salir' para terminar): ")
    
    # Si el usuario escribe 'salir', terminamos el bucle
    if producto.lower() == 'salir':
        break
    
    # Agregamos el producto a la lista de inventario
    inventario.append(producto)

# Mostramos todos los productos ingresados al inventario
print("\nInventario de productos:")
for item in inventario:
    print(f"- {item}")
