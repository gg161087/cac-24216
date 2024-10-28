'''
Registro de productos en un inventario    
    Vas a implementar un sistema básico para registrar productos en el inventario de una tienda. El programa debe permitir 
    que el usuario agregue productos a una lista hasta que decida no agregar más. Luego, deberás mostrar todos los 
    productos ingresados al inventario.
    Tips:
    ● Usá una lista para almacenar los productos. Diseña la lista pensando en el TFI.

Consultar el stock de productos
    Tu programa debe permitir al usuario consultar el inventario de una tienda para verificar si un producto está en stock. Si 
    el producto está en la lista, el programa debe informarlo, si no, debe mostrar un mensaje indicando que no está 
    disponible.
    Tips:
    ● Usá una lista para almacenar los productos en stock.
    ● Permití que el usuario ingrese el nombre de un producto a consultar.
    ● Recorré la lista con un bucle while para verificar si el producto está en stock.
'''
def validate_name(input_str):
    return len(input_str) >= 3 and not input_str.isnumeric()

def validate_stock(input_str):
    return input_str.isnumeric() and int(input_str) > 0

def validate_price(input_str):
    return input_str.replace('.', '', 1).isdigit() and float(input_str) > 0

def validated_input(prompt, current_value, validation_func=None, allow_skip=True):
    input_valido = False  # Variable de control para el bucle
    while not input_valido:
        try:
            user_input = input(prompt).title() if 'nombre' in prompt.lower() else input(prompt)
            if user_input == '-1':
                return -1  
            if user_input == '' and allow_skip:
                return current_value
            if validation_func and not validation_func(user_input):
                print('Entrada inválida. Inténtalo de nuevo.')
            else:
                input_valido = True  # Cambiar la bandera a True si la entrada es válida
                return user_input
        except ValueError as ve:
            print(f'Error en la entrada: {ve}. Inténtalo de nuevo.')
        except Exception as e:
            print(f'Ocurrió un error inesperado: {e}. Inténtalo de nuevo.')

def add_product():
    """Función para agregar productos al inventario."""
    print('Para salir escribir "-1"')
    print('Agregar un producto.')
    back = False
    name = ''
    stock = 0
    price = 0
    inventory = []
    
    while not back:
        try:
            # Obtener nombre del producto
            name = validated_input('Nombre del producto: ', name, validate_name, allow_skip=False)
            if name == -1:
                back = True
                break
            # Obtener stock del producto
            stock = validated_input(f'Stock de {name}: ', stock, validate_stock)
            if stock == -1:
                back = True
                break
            stock = int(stock)
            # Obtener precio del producto
            price = validated_input(f'Precio de {name}: ', price, validate_price)
            if price == -1:
                back = True
                break
            price = float(price)
            # Crear el producto si no se vuelve
            if not back:
                new_product = {
                    "name": name,
                    "stock": int(stock),
                    "price": float(price)
                }            
                # Agregar el producto al inventario
                inventory.append(new_product)                 
            # Preguntar si el usuario quiere agregar otro producto
            agregar_mas = input("¿Desea agregar otro producto? (s/n): ").lower()
            if agregar_mas != 's':
                back = True
        except ValueError as ve:
            print(f'Error en la conversión de datos: {ve}')
        except Exception as e:
            print(f'Ocurrió un error inesperado: {e}')    
    return inventory

def check_stock(inventory, product_name):
    """Función para consultar si un producto está en stock."""    
    if len(inventory) > 0:
        for product in inventory:
            if product["name"].lower() == product_name.lower():
                if product['stock'] > 0:
                    print(f"El producto '{product['name']}' está en stock con {product['stock']} unidades.")                
                else:
                    print(f"El producto '{product['name']}' No tiene stock: {product['stock']} unidades.")
            else:
                print(f"El producto '{product_name}' no está disponible en el inventario.")
    else:
        print('El inventario esta vacio.')    

# Ejecución del programa
inventory = add_product()
print('Para salir escribir "-1"')
found = False
while not found:
    product_name = input("\nIngrese el nombre del producto a consultar: ")
    if product_name == '-1':
        found = True
        break
    check_stock(inventory, product_name)
