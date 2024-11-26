import os

def funcion_1():
    print("Ejecutando Función 1")

def funcion_2():
    print("Ejecutando Función 2")

def funcion_3():
    print("Ejecutando Función 4")

def funcion_4():
    print("Ejecutando Función 4")

def funcion_5():
    print("Ejecutando Función 5")

def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("5. Opción 5")
    print("7. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ")
        if opcion == '1':
            funcion_1()
        elif opcion == '2':
            funcion_2()
        elif opcion == '3':
            funcion_3()
        elif opcion == '4':
            funcion_4()
        elif opcion == '5':
            funcion_5()
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
