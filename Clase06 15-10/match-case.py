#desde la version 3.10

option = int(input("Ingrese opcion: "))

match option:
    case 1:
        print("Alta")
    case 2: 
        print("Baja")
    case 3:
        print("Modificar")
    case _:
        print("Opcion no valida")