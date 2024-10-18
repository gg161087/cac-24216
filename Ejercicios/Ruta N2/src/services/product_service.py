from src.models.product_model import create_product, get_products, get_product, update_product, delete_product

def add_product():
    print('Para volver al menu anterior escribir "-1"')
    volver = False
    prompt = ''
    name = ''
    stock = 0
    price = 0
    while not volver:    
        while len(name) == 0 and len(name) < 3:                         
            prompt = input('Nombre del producto: ').title()
            if prompt == '-1':
                volver = True
                break
            else:  
                if prompt.isnumeric() or len(prompt) < 3:
                    print('El nombre del producto debe contener letras y más de 3 caracteres.')            
                else:
                    name = prompt
        while stock == 0 and prompt != '-1':                      
            prompt = input(f'Stock de {name}: ')
            if prompt == '-1':
                volver = True 
                break
            else:
                if prompt.isnumeric() and int(prompt) > 0:
                    stock = int(prompt)
                else:
                    print('El stock debe ser numerico y mayor que 0.')   
        while price == 0 and prompt != '-1':
            prompt = input(f'Precio de {name}: ')
            if prompt == '-1':
                volver = True 
                break
            else:                
                if prompt.isnumeric() and prompt != 0:   
                    price = float(prompt)
                else:
                    print('El precio debe ser numerico y mayor que 0.')  
        if not volver:
            new_product = {
                "name": name,
                "stock" : stock,
                "price" : price
            }
            create_product(new_product)
            print(f'Producto "{name}" agregado con éxito.')
            volver = True                

def list_products():
    products = get_products()
    if not products:
        print('La lista de productos está vacía.')
    else:
        print(f'{"#":<5} {"Producto":<15} {"Stock":>15} {"Precio($)":>15}')
        for product in products:
            print(f"{product['id']:<5} {product['name']:<15} {product['stock']:>15} {product['price']:>15.2f}")

def list_product():
    print('Para volver al menu anterior escribir "-1"')    
    volver = False
    while not volver:
        prompt = input('Ingrese el ID del producto: ')            
        if prompt == '-1':
            volver = True
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
    
    

def modify_product():
    print('Para volver al menu anterior escribir "-1"')
    volver = False
    prompt = ''
    product_id = 0
    new_name = ''
    new_stock = 0
    new_price = 0
    product = {}
    while not volver:
        while product_id == 0:
            prompt = input('Ingrese el ID del producto a actualizar: ')
            if prompt == '-1':
                volver = True
                break
            else:
                if prompt.isnumeric() and int(prompt) > 0:
                    product_id = int(prompt)
                    product = get_product(product_id)
                    print(product)
                else:
                    print('El ID del producto debe ser numerico y mayor que 0.')
        while len(new_name) == 0 and len(new_name) < 3:
            prompt = input('Nuevo nombre del producto (presiona Enter para no cambiarlo): ').title()
            if prompt == '-1':
                volver = True
                break
            else:
                if prompt == '':
                    new_name = product['name']
                else:  
                    if prompt.isnumeric() or len(prompt) < 3:
                        print('El nombre del producto debe contener letras y más de 3 caracteres.')            
                    else:
                        new_name = prompt
        while new_stock == 0 and prompt != '-1':                      
            prompt = input('Nuevo stock del producto (presiona Enter para no cambiarlo): ')
            if prompt == '-1':
                volver = True 
                break
            else:
                if prompt == '':
                    new_stock = product['stock']
                else:
                    if prompt.isnumeric() and int(prompt) > 0:
                        new_stock = int(prompt)
                    else:
                        print('El stock debe ser numerico y mayor que 0.')
        while new_price == 0 and prompt != '-1':
            prompt = input('Nuevo precio del producto (presiona Enter para no cambiarlo): ')
            if prompt == '-1':
                volver = True 
                break
            else:
                if prompt == '':
                    new_price = product['price']
                else:                    
                    if prompt.isnumeric() and prompt != 0:   
                        new_price = float(prompt)
                    else:
                        print('El precio debe ser numerico y mayor que 0.')
        new_data = {
            "id" : product_id,
            "name" : new_name,
            "stock" : new_stock,
            "price" : new_price
        }
        if update_product(product_id, new_data):
            print('Producto actualizado con éxito.')
            volver = True
        else:
            print(f'No se encontró un producto con ID {product_id}.')

def remove_product():
    print('Para volver al menu anterior escribir "-1"')
    volver = False
    while not volver:        
        prompt = input('Ingrese el número de ID del producto a eliminar: ')
        if prompt == '-1':
            volver = True 
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