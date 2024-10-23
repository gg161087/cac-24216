'''
Control de stock de productos
    Desarrollá un programa que permita al usuario ingresar el nombre de varios productos y la cantidad en stock que hay de 
    cada uno. El programa debe seguir pidiendo que ingrese productos hasta que el usuario decida salir, ingresando "salir" 
    como nombre de producto. Después de que el bucle termine, el programa debe mostrar la cantidad total de productos 
    ingresados.
    Tips:
    ● Vas a necesitar un contador.
    ● Tené presente las estructuras condicionales.

Validación de precios de productos
    Optativos | No entregables
    Escribí un programa que permita al usuario ingresar el precio de un producto, pero que sólo acepte valores mayores a 0. 
    Si el usuario ingresa un valor inválido (negativo o cero), el programa debe mostrar un mensaje de error, y volver a pedir 
    el valor hasta que se ingrese uno válido. Al final, el programa debe mostrar el precio aceptado.
    Tips:
    ● Antes de empezar, pensá si es necesario usar contadores o acumuladores.
    ● Recordá que input() siempre devuelve cadenas de caracteres.

'''

#Control de stock de productos
def control_stock():
    contador_productos = 0
    stock_productos = {}
    continuar = True
    while continuar:
        producto = input('Ingrese el nombre del producto (o "salir" para terminar): ').strip().lower()
        if producto == "salir":
            continuar = False
        else:
            try:
                cantidad = int(input(f'Ingrese la cantidad en stock para {producto}: '))
                if cantidad < 0:
                    raise ValueError
            except ValueError:
                print('Error: Debe ingresar una cantidad válida y positiva.')
                continue
            stock_productos[producto] = cantidad
            contador_productos += 1
    print('\nResumen de productos ingresados:')
    for producto, cantidad in stock_productos.items():
        print(f'{producto}: {cantidad} unidades')
    print(f'\nCantidad total de productos ingresados: {contador_productos}')

#Validación de precios de productos
def validacion_precio():
    bandera = True
    while bandera:
        try:
            precio = float(input('Ingrese el precio del producto: '))
            if precio > 0:
                bandera = False  # Cambia la bandera a False si el precio es válido
            else:
                print('Error: el precio debe ser mayor a 0.')
        except ValueError:
            print('Error: debe ingresar un valor numérico válido.')    
    print(f'El precio aceptado es: ${precio:.2f}')


control_stock()   
validacion_precio()