from src.models.product_model import create_product, get_products, get_product, update_product, delete_product

def add_product():
    name = input("Nombre del producto: ")
    stock = int(input("Stock disponible: "))
    price = float(input("Precio del producto: "))
    new_product = {
        "name": name,
        "stock" : stock,
        "price" : price
    }
    create_product(new_product)
    print(f"Producto '{name}' agregado con éxito.")

def list_products():
    products = get_products()
    if not products:
        print("La lista de productos está vacía.")
    else:
        for product in products:
            print(f"ID: {product['id']}, Nombre: {product['name']}, Stock: {product['stock']}, Precio: {product['price']}")

def list_product():
    product_id = int(input("Ingrese el ID del producto: "))
    product = get_product(product_id)
    
    if product:
        print(f"ID: {product['id']}")
        print(f"Nombre: {product['name']}")
        print(f"Stock: {product['stock']}")
        print(f"Precio: ${product['price']:.2f}")
    else:
        print(f"No se encontró un producto con ID {product_id}.")

def modify_product():
    product_id = int(input("Ingrese el ID del producto a actualizar: "))
    new_name = input("Nuevo nombre del producto (presiona Enter para no cambiarlo): ")
    new_stock = input("Nuevo stock del producto (presiona Enter para no cambiarlo): ")
    if len(new_stock) > 0:
        new_stock = int(new_stock)
    new_price = (input("Nuevo precio del producto (presiona Enter para no cambiarlo): "))
    if len(new_price) > 0:
        new_price = float(new_price)
    new_data = {
        "id" : product_id,
        "name" : new_name,
        "stock" : new_stock,
        "price" : new_price
    }
    if update_product(product_id, new_data):
        print("Producto actualizado con éxito.")
    else:
        print(f"No se encontró un producto con ID {product_id}.")

def remove_product():
    product_id = int(input("Ingrese el ID del producto a eliminar: "))    
    if delete_product(product_id):
        print(f"Producto con ID {product_id} eliminado con éxito.")
    else:
        print(f"No se encontró un producto con ID {product_id}.")