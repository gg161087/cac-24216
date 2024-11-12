def validate_name(input_str):
    return len(input_str) >= 3 and not input_str.isnumeric()

def validate_stock(input_str):
    return input_str.isnumeric() and int(input_str) > 0

def validate_price(input_str):
    return input_str.replace('.', '', 1).isdigit() and float(input_str) > 0

def validated_input(prompt, current_value, validation_func=None, allow_skip=True):
    input_valid = False  # Variable de control para el bucle
    while not input_valid:
        try:
            user_input = input(prompt).title() if 'nombre' in prompt.lower() else input(prompt)

            if user_input == '-1':
                return -1  

            if user_input == '' and allow_skip:
                return current_value

            if validation_func and not validation_func(user_input):
                print('Entrada inválida. Inténtalo de nuevo.')
            else:
                input_valid = True  # Cambiar la bandera a True si la entrada es válida
                return user_input

        except ValueError as ve:
            print(f'Error en la entrada: {ve}. Inténtalo de nuevo.')
        except Exception as e:
            print(f'Ocurrió un error inesperado: {e}. Inténtalo de nuevo.')
