from os import system
from src.views.product_view import display_menu
from src.services.product_service import add_product, list_products, retrieve_product, edit_product, delete_product_by_id, low_stock_report

def product_menu():
    system('cls')
    while True:        
        display_menu()
        prompt = input("Seleccione una opción: ")
        if prompt.isnumeric():
            option = int(prompt)
            if option > 0 and option <= 7:
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
                        low_stock_report()
                    case 6:
                        system('cls')
                        delete_product_by_id()
                    case 7:
                        print('Saliendo del programa...')
                        break
            else:
                system('cls')
                print('\t Opción no válida, intente de nuevo: ')    
        else:
            system('cls')
            print('\t Opción no válida, intente de nuevo: ')
