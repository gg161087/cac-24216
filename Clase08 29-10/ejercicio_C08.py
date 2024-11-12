'''
Registro de ventas por día
    Desarrollá un programa que permita registrar las ventas diarias de un comercio durante 5 días. Al finalizar, el sistema 
    debe mostrar el total de ventas realizadas en cada día y el promedio de ventas.
    Tips:
        ● Usá un bucle while que permita al usuario ingresar el monto de las ventas diarias.
        ● Asegurate de validar que el monto ingresado sea un valor positivo.
        ● Usá un acumulador para la suma de las ventas.

Actualización del inventario a partir de un arreglo
    En una tienda, es necesario actualizar el inventario cuando se venden productos. A continuación, te proporcionamos un 
    arreglo con una lista de productos, donde cada producto tiene un código, una descripción y una cantidad en stock. 
    Escribí un programa que permita:
        ● Seleccionar un producto a partir de su código.
        ● Ingresar la cantidad vendida (que debe ser mayor que cero).
        ● Actualizar la cantidad en stock de ese producto restando la cantidad vendida.
    El arreglo de productos disponibles es que ves a continuación.
    El script que tenés que hacer debe modificar la cantidad en stock de acuerdo a cada venta realizada. Si la cantidad 
    vendida es mayor que la cantidad disponible en stock, el programa debe mostrar un mensaje de error.
    productos = [
        ["P001", "Manzanas", 50],
        ["P002", "Peras", 40],
        ["P003", "Bananas", 30],
        ["P004", "Naranjas", 60]
    ]
'''
def registro_ventas():
    # Lista para almacenar las ventas diarias
    ventas_por_dia = []
    # Registro de ventas por 5 días
    dias = 5
    contador_dias = 1
    while contador_dias <= dias:
        venta_dia = input(f"Ingresá el monto de las ventas para el día {contador_dias}: ")        
        # Validación de que el monto sea un número positivo
        try:
            venta_dia = float(venta_dia)
            if venta_dia > 0:
                ventas_por_dia.append(venta_dia)
                contador_dias += 1
            else:
                print("El monto debe ser un valor positivo. Intentalo nuevamente.")
        except ValueError:
            print("Por favor, ingresá un número válido.")
    # Mostrar ventas diarias
    print("\nResumen de ventas diarias:")
    for i, venta in enumerate(ventas_por_dia, start=1):
        print(f"Día {i}: ${venta:.2f}")
    # Calcular y mostrar el total de ventas y el promedio
    total_ventas = sum(ventas_por_dia)
    promedio_ventas = total_ventas / dias
    print(f"\nTotal de ventas en los 5 días: ${total_ventas:.2f}")
    print(f"Promedio de ventas diarias: ${promedio_ventas:.2f}")

def actualizar_inventario():
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