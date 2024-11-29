def table_headers():
    print(f'{"#":<5} {"Producto":<15} {"Stock":>15} {"Precio($)":>15}')

def display_product(product):    
    print(f'{product['id']:<5} {product['name']:<15} {product['stock']:>15} {product['price']:>15.2f}')

def display_products(products):
    table_headers()
    for product in products:
        display_product(product)

def display_back_menu():
    print('Para volver al menú anterior escriba la letra "v"')

def display_product_requirements():
    print('El nombre debe tener al menos 3 caracteres, stock numérico y precio numérico/mayor que 0.')
