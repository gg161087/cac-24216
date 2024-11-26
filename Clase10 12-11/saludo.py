#funciones predefinidas de python
# type()
# print()
# input()

#creamos nuestras propias funciones
#funcion sin argumentos y sin retorno de valor
# definir la funcion
def saludar_user():
    """
    Muestra un simple saludo
    sin parámetros
    desarrollado por gmedina
    """
    print("Hola! desde la función")
    
#invocar 
print("Función sin argumentos: ")
saludar_user()
print("continúa el programa...")
#muestro los docstring - doc de las funciones
help(saludar_user)
print(saludar_user.__doc__)


    