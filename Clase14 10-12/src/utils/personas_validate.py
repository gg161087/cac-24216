from src.utils.displayer import display_invalid_data

def validate_back(prompt):
    return prompt.lower() == 'v'

def validate_id(id):
    return validate_back(id) and id.isnumeric() and int(id) > 0

def validate_edad(edad):
    return validate_back(edad) and id.isnumeric() and int(id) > 0

def validate_nombre(nombre):
    return validate_back(nombre) and len(nombre) >= 3 and not nombre.isnumeric()

def validate_ciudad(ciudad):
    return validate_back(ciudad) and len(ciudad) >= 3 and not ciudad.isnumeric()

def validated_input(prompt, current_value, validation_func=None, allow_skip=True):
    input_valid = False  # Variable de control para el bucle
    while not input_valid:
        try:
            user_input = input(prompt).title() if 'nombre' in prompt.lower() else input(prompt)
            if user_input.lower() == 'v':                
                return 'v'
            if user_input == '' and allow_skip:
                return current_value
            if validation_func and not validation_func(user_input):                               
                display_invalid_data()
            else:
                input_valid = True  # Cambiar la bandera a True si la entrada es válida
                return user_input
        except ValueError as ve:
            print(f'Error en la entrada: {ve}. Inténtalo de nuevo.')
        except Exception as e:
            print(f'Ocurrió un error inesperado: {e}. Inténtalo de nuevo.')