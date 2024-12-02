from colorama import Fore, Back, init
init(autoreset=True)

def display_divider():
    print(Fore.YELLOW + '-' * 53)

def table_headers():
    print(f'{"#":<5} {"Producto":<15} {"Stock":>15} {"Precio($)":>15}')

def display_product(product):    
    print(f'{product['id']:<5} {product['name']:<15} {product['stock']:>15} {product['price']:>15.2f}')

def display_products(products):
    display_divider()
    table_headers()
    for product in products:
        display_product(product)

def display_back_menu():
    display_divider()
    print(f'Para volver al menú anterior escriba la letra {Fore.YELLOW}"v"')
    display_divider()

def display_product_requirements():
    print('El nombre debe tener al menos 3 caracteres, stock numérico y precio numérico/mayor que 0.')

def display_menu():
    display_divider()
    print('Menú E-commerce, Escriba número de opcion (1-7):'.center(50))
    print(Fore.GREEN + '\t 1. Agregar Producto')
    print(Fore.YELLOW + '\t 2. Listar Productos')
    print(Fore.BLUE + '\t 3. Buscar Producto')
    print(Fore.MAGENTA + '\t 4. Editar Producto')
    print(Fore.CYAN + '\t 5. Reporte Productos bajo de Stock')
    print(Fore.RED + '\t 6. Eliminar Producto')
    print('\t 7. Salir')
    display_divider()