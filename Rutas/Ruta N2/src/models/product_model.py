from src.data.database import list_products

def create_product(product):
    if not list_products:
        id_new = 1
    else:
        id_new = int(max(list_products, key=lambda x:x['id'])['id']) + 1
    product['id'] = id_new
    list_products.append(product)

def get_products():    
    return list_products

def get_product(product_id):
    for product in list_products:
        if product.get('id') == product_id:
            return product
    return None 

def update_product(product_id, new_data):
    for product in list_products:
        if product.get('id') == product_id:
            if new_data['name'] == "":
                new_data['name'] = product['name']
            if new_data['stock'] == "":
                new_data['stock'] = product['stock']
            if new_data['price'] == "":
                new_data['price'] = product['price']
            product.update(new_data)
            return True
        else:
            False 

def delete_product(product_id):
    for i, product in enumerate(list_products):
        if product.get('id') == product_id:
            list_products.pop(i)
            return True 
    return False