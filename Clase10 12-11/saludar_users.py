#pasando lista como argumento

#mensaje = 'Bienvenidos' #variable global

def saludar_usuarios(nombres):
    """mostrar un saludo a cada user en la lista"""
    for nombre in nombres:
        mensaje = f"Hola {nombre}!"
        print(mensaje) #variables locales

def crear_ficha_user():
    pass
def consultar_user():
    pass

#invocar - main - principal
#print(mensaje) #error
usernames = ['gmedina', 'plopez', 'sgomez', 'lmesa']
saludar_usuarios(usernames)
#username = 'sarasa'
username = ['sarasa']
saludar_usuarios(username)
crear_ficha_user()
        
        