import time
from src.utils.displayer import (
    display_divider, 
    display_personas, 
    display_persona_requirements, 
    display_title_menu,
    display_back_menu, 
    display_table_headers, 
    display_persona, 
    display_confirm,
    clear_screen,
    display_not_found,
    display_invalid_option
)
from src.utils.personas_validate import (
    validate_back, 
    validate_id,     
    validate_nombre, 
    validate_edad, 
    validate_ciudad,
    validated_input
)
from src.controller.personas_controller import (
    create_persona_controller
)

def create_persona_view():
    while True:
        display_title_menu('Agregar Persona', 'V', 'letra')
        display_back_menu()
        display_persona_requirements()
        nombre = validated_input('\tIngrese el NOMBRE de la persona: ', validate_nombre, allow_skip=False)
        if validate_back(nombre):
            clear_screen() 
            break
        display_divider()
        edad = validated_input('\tIngrese la EDAD de la persona: ', validate_edad, allow_skip=False)
        if validate_back(edad):
            clear_screen() 
            break
        display_divider()
        ciudad = validated_input('\Ingrese la CIUDAD de la persona: ', validate_ciudad, allow_skip=False)
        if validate_back(ciudad):
            clear_screen() 
            break
        display_divider()
        if nombre and edad and ciudad:
            if create_persona_controller(nombre, edad, ciudad):
                clear_screen()
                display_divider()
                print(f'Persona "{nombre}" agregado con éxito.')
                display_divider()  
                break
            else:
                print('hubo un error al agregar a la persona, intente de nuevo')
