#pasando información a la funcion
#funciones con parámetros
def saludar_user(username, password): #parámetros posicionales
    """Mostrar un simple saludo personalizado
    Params:
        username: nombre del user
    """
    print(f"Hola {username}! Password ingresada es: {password}")
    
#invocar con argumentos
saludar_user('gmedina', 123) #argumento por valor
nombre = input("Ingrese su nombre de usuario: ")
contrasenia = input("Contraseña: ")
saludar_user(nombre, contrasenia) #argumento por referencia
#saludar_user() #error