from src.utils.validate_input_product import validate_name, validate_price, validate_stock, validated_input
from src.models.product_model import create_product, get_products, get_product, update_product, delete_product

def add_product():
    print('Para volver al menú anterior escribir "-1".')
    print('El nombre debe tener al menos 3 caracters, stock numérico y precio numérico/mayor que 0.')
    back = False
    name = ''
    stock = 0
    price = 0

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
                    "stock": stock,
                    "price": price
                }
                create_product(new_product)
                print(f'Producto "{name}" agregado con éxito.')
                back = True
        except ValueError as ve:
            print(f'Error en la conversión de datos: {ve}')
        except Exception as e:
            print(f'Ocurrió un error inesperado: {e}')

def list_products():
    products = get_products()
    if not products:
        print('La lista de productos está vacía.')
    else:
        print(f'{"#":<5} {"Producto":<15} {"Stock":>15} {"Precio($)":>15}')
        for product in products:
            print(f"{product['id']:<5} {product['name']:<15} {product['stock']:>15} {product['price']:>15.2f}")

def retrieve_product():
    print('Para volver al menu anterior escribir "-1"')    
    back = False
    while not back:
        prompt = input('Ingrese el ID del producto: ')            
        if prompt == '-1':
            back = True
            break
        else:
            if prompt.isnumeric() and int(prompt) > 0:
                product_id = int(prompt)
                product = get_product(product_id)
                if product:
                    print(f'{"#":<5} {"Producto":<15} {"Stock":>15} {"Precio($)":>15}')
                    print(f"{product['id']:<5} {product['name']:<15} {product['stock']:>15} {product['price']:>15.2f}")
                else:
                    print(f'No se encontró un producto con ID {product_id}.')
            else:
                print('El ID del producto debe ser numerico y mayor que 0.')

def edit_product():
    print('Para volver al menú anterior escribir "-1"')
    back = False
    product_id = 0
    product = {}

    while not back:
        # Obtener ID del producto
        prompt = validated_input('Ingrese el ID del producto a actualizar: ', '', allow_skip=False)
        if prompt == -1:
            return  # Salir si se desea volver al menú anterior
        elif prompt.isnumeric() and int(prompt) > 0:
            product_id = int(prompt)
            product = get_product(product_id)  # Suponiendo que esta función obtiene el producto
            if not product:
                print(f'No se encontró un producto con ID {product_id}.')
                continue
            print(product)  # Mostrar el producto actual
        else:
            print('El ID del producto debe ser numérico y mayor que 0.')
            continue  # Volver al inicio del bucle

        # Obtener nuevo nombre
        new_name = validated_input('Nuevo nombre del producto (presiona Enter para no cambiarlo): ', product['name'], validate_name)
        
        # Obtener nuevo stock
        new_stock_str = validated_input('Nuevo stock del producto (presiona Enter para no cambiarlo): ', str(product['stock']), validate_stock)
        new_stock = int(new_stock_str) if new_stock_str else product['stock']  # Usar el valor actual si se presiona Enter

        # Obtener nuevo precio
        new_price_str = validated_input('Nuevo precio del producto (presiona Enter para no cambiarlo): ', str(product['price']), validate_stock)
        new_price = float(new_price_str) if new_price_str else product['price']  # Usar el valor actual si se presiona Enter

        # Crear nuevo diccionario de datos
        new_data = {
            "id": product_id,
            "name": new_name,
            "stock": new_stock,
            "price": new_price
        }

        # Actualizar producto
        if update_product(product_id, new_data):
            print('Producto actualizado con éxito.')
        else:
            print(f'No se pudo actualizar el producto con ID {product_id}.')
        
        back = True  # Salir del bucle después de la actualización

def remove_product():
    print('Para volver al menu anterior escribir "-1"')
    back = False
    while not back:        
        prompt = input('Ingrese el número de ID del producto a eliminar: ')
        if prompt == '-1':
            back = True 
            break
        else:
            if prompt.isnumeric() and int(prompt) > 0:
                product_id = int(prompt)      
                if delete_product(product_id):
                    print(f'Producto con ID {product_id} eliminado con éxito.')
                else:
                    print(f'No se encontró un producto con ID {product_id}.')
            else:
                print('El ID tiene que ser numerico y mayor que 0.')