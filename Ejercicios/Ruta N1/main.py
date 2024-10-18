from os import system
from product_service import add_product, list_products, list_product, modify_product, remove_product, edit_product

def main():
    while True:
        print('_' * 50)
        print('Menú E-commerce, Escriba número de opcion (1-6):'.center(50))
        print('\t 1. Agregar producto')
        print('\t 2. Listar productos')
        print('\t 3. Mostrar producto por ID')
        print('\t 4. Actualizar producto')
        print('\t 5. Eliminar producto por ID')
        print('\t 6. Salir')
        prompt = input('Selecciona una opción: ')

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
                        list_product()
                    case 4:
                        system('cls')
                        edit_product()
                    case 5:
                        system('cls')
                        remove_product()
                    case 6:
                        break
            else:
                system('cls')
                print('\t Opción no válida, intente de nuevo: ')    
        else:
            system('cls')
            print('\t Opción no válida, intente de nuevo: ')        

if __name__ == '__main__':
    main()