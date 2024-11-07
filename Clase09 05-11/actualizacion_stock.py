# Lista de productos con código, descripción y cantidad en stock
productos = [
   ["P001", "Manzanas", 50],
   ["P002", "Peras", 40],
   ["P003", "Bananas", 30],
   ["P004", "Naranjas", 60]
]

# Pedir al usuario el código del producto
codigo = input("Ingresá el código del producto: ").strip()

# Buscar el producto en la lista
producto_encontrado = None
for producto in productos:
    if producto[0] == codigo:
        producto_encontrado = producto
        break

# Validar si el producto fue encontrado
if producto_encontrado:
    print(f"Producto seleccionado: {producto_encontrado[1]} - Stock disponible: {producto_encontrado[2]}")

    # Pedir al usuario la cantidad vendida y validarla
    try:
        cantidad_vendida = int(input("Ingresá la cantidad vendida: "))

        if cantidad_vendida <= 0:
            print("Error: La cantidad vendida debe ser mayor que cero.")
        elif cantidad_vendida > producto_encontrado[2]:
            print("Error: La cantidad vendida es mayor que el stock disponible.")
        else:
            # Actualizar el stock restando la cantidad vendida
            producto_encontrado[2] -= cantidad_vendida
            print(f"Venta registrada. Nuevo stock de {producto_encontrado[1]}: {producto_encontrado[2]}")

    except ValueError:
        print("Error: Ingresá un número válido para la cantidad vendida.")
else:
    print("Error: Código de producto no encontrado.")
