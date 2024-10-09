'''
CONDICIONALES:
    Simple:
        Pseudocodigo:
            si edad >= 18 entonces
                escribir "mayor de edad"
            finsi
        Python:
            if edad >=18:
                print('mayor de edad')
                
    Doble:
        Pseudocodigo:
            si edad >= 18 entonces
                escribir "mayor de edad"
            finsi
            sino
                escribir "es menor de edad"
            finsino
        Python:
            if edad >=18:
                print('mayor de edad')
            else:
                print('Es menos de edad')

    Anidamiento:
        USERNAME = 'admin'
        PASSWORD = '123456'
        user_name = input('Ingrese su nombre: ')       
        if user_name == NAME:
            user_password = input('Ingrese su contraseña: ')
            if user_password == PASSWORD:
                print('Inicio exitoso')
            else:
                print('Contraseña incorrecta')
        else:
            print('usuario incorrecto')
        #Por cuestiones de seguridad de hace de la siguiente forma:
        user_name = input('Ingrese su nombre: ')  
        user_password = input('Ingrese su contraseña: ')
        if user_name == NAME and user_password == PASSWORD:
            print('Inicio exitoso')
        else:
            print('usuario o Contraseña incorrecta')

    Multiple:


'''