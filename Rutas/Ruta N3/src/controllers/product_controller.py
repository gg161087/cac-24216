from os import system
from src.services.product_service import add_product, list_products, retrieve_product, edit_product, delete_product_by_id

def product_menu():
    system('cls')
    while True:        
        print('_' * 50)
        print('Menú E-commerce, Escriba número de opcion (1-6):'.center(50))
        print('1. Agregar Producto')
        print('2. Listar Productos')
        print('3. Buscar Producto')
        print('4. Editar Producto')
        print('5. Eliminar Producto')
        print('6. Salir')
        prompt = input("Seleccione una opción: ")
        if prompt.isnumeric():
            option = int(prompt)
            if option > 0 and option <= 6:
                match option:
                    case 1:
                        system('cls')
                        add_product()
                    case 2:
                        system('cls')
                        list_products() 
                    case 3:  
                        system('cls')
                        retrieve_product()
                    case 4:
                        system('cls')
                        edit_product()
                    case 5:
                        system('cls')
                        delete_product_by_id()
                    case 6:
                        print('Saliendo del programa...')
                        break
            else:
                system('cls')
                print('\t Opción no válida, intente de nuevo: ')    
        else:
            system('cls')
            print('\t Opción no válida, intente de nuevo: ')
