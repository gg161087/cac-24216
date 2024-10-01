from os import system
from product_service import add_product, list_products, list_product, modify_product, remove_product

def main():
    while True:
        print('\nMenú E-commerce, Escriba el número de la opcion deseada:')
        print('\t 1. Agregar producto')
        print('\t 2. Listar productos')
        print('\t 3. Mostrar producto por ID')
        print('\t 4. Actualizar producto')
        print('\t 5. Eliminar producto por ID')
        print('\t 6. Salir')
        option = input('Selecciona una opción: ')

        if option == '1':
            system('cls')
            add_product()
        elif option == '2':
            system('cls')
            list_products()
        elif option == '3':
            system('cls')
            list_product()
        elif option == '4':
            system('cls')
            modify_product()
        elif option == '5':
            system('cls')
            remove_product()
        elif option == '6':
            break
        else:
            system('cls')
            print('\t Opción no válida, intente de nuevo:')        

if __name__ == '__main__':
    main()