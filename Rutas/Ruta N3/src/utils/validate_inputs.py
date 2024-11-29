def validate_name(name):
    return len(name) >= 3 and not name.isnumeric()

def validate_price(price):
    return price.replace('.', '', 1).isdigit() and float(price) > 0

def validate_stock(stock):
    return stock.isnumeric() and int(stock) >= 0

def validated_input(prompt, current_value, validation_func=None, allow_skip=True):
    input_valid = False  # Variable de control para el bucle
    while not input_valid:
        try:
            user_input = input(prompt).title() if 'nombre' in prompt.lower() else input(prompt)

            if user_input == 'v':
                return 'v'

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

def validate_back(prompt):
    if prompt == 'v':
        return True