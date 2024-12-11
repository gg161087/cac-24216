import time
from src.utils.displayer import (
    display_divider, 
    display_personas, 
    display_product_requirements,
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
    validate_ciudad
)
from src.services.personas_service import (
    add_persona,
    get_all_personas,
    search_persona,
    update_persona,
    delete_persona
)

def create_persona_controller(nombre, edad, ciudad):
    if add_persona(nombre, int(edad), ciudad):
        return True
    else:
        False
        """
        persona = search_persona('nombre', nombre)
        if persona:
            clear_screen()
            display_divider()
            print(f'Producto "{name}" agregado con éxito.')
            display_divider()
        else:
            False
        """        

def list_personas_controller():
    personas = get_all_personas()
    if personas:
        display_personas(personas, 'LISTADO de PERSONAS')
    else:
        display_not_found('PERSONAS')        
        time.sleep(3)

def search_persona_controller():
    display_back_menu()
    back = False
    while not back:
        prompt = input(f'\t Ingrese el NOMBRE del producto a BUSCAR: ').strip()           
        if not validate_back(prompt) and (back := True):
            clear_screen()
            break
        else:
            if validate_nombre(prompt):
                nombre = prompt.capitalize()
                persona = search_persona('name', nombre)
                if persona:
                    clear_screen()
                    display_back_menu()
                    display_table_headers()
                    display_persona(persona)
                    display_divider()                    
                else:
                    display_not_found(f'Persona con NOMBRE: {nombre}')
            else:
                print('El NOMBRE del producto debe tener al menos 3 caracteres.')
                

def remove_persona_controller():
    display_back_menu() 
    back = False
    confirm = False
    while not back:
        prompt = input(f'\t Ingrese el ID de la persona a ELIMINAR: ').strip()           
        if not validate_back(prompt) and (back := True):
            clear_screen()
            break
        else:
            if validate_id(prompt):
                id = int(prompt)
                persona = search_persona('id', id)
                if persona:
                    clear_screen()
                    display_divider()
                    display_table_headers()
                    display_persona(persona)
                    display_divider()
                    display_confirm('ELIMINAR')
                    while not confirm:
                        prompt_confirm = input('\t Seleccione una opción: ').strip().lower()
                        if prompt_confirm == 's':
                            if delete_persona(int(persona['id'])):                                    
                                break
                        elif prompt_confirm == 'n':
                            clear_screen()
                            display_back_menu()
                            break                            
                        else:
                            display_invalid_option()                                                                    
                    else:
                        display_not_found(f'persona con ID: {id}')                 
                else:
                    print('El ID de la persona debe ser numerico y mayor que 0.')
                                         
def update_persona_controller():
    display_back_menu()
    back = False
    while not back:
        prompt = input(f'\t Ingrese el ID de la persona a ACTUALIZAR: ').strip()           
        if not validate_back(prompt) and (back := True):
            clear_screen()
            break
        else:                        
            if validate_id(prompt):
                id = int(prompt)
                persona = search_persona('id', id)
                if persona:
                    #funcion para pedir los datos para actualizar
                    pass          
                else:
                    display_not_found(f'Persona con ID: {id}')
