from os import system
from src.services.product_service import add_product, list_products, list_product, modify_product, remove_product

def main():
    while True:
        print("\nMenú E-commerce")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Mostrar producto por ID")
        print("4. Actualizar producto")
        print("5. Eliminar producto por ID")
        print("6. Salir")
        option = input("Selecciona una opción: ")

        if option == "1":
            system('cls')
            add_product()
        elif option == "2":
            system('cls')
            list_products()
        elif option == "3":
            system('cls')
            list_product()
        elif option == "4":
            system('cls')
            modify_product()
        elif option == "5":
            system('cls')
            remove_product()
        elif option == "6":
            break
        else:
            print("Opción no válida")        

if __name__ == "__main__":
    main()