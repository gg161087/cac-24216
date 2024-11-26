import os
from src.controllers.artists_controller import add_artist,show_all_artists, show_artist_by_id, update_artist, delete_artist

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    bandera = True
    while bandera:        
        print('\n' + '=' * 40)
        print(' ' * 10 + '🎶GESTIÓN DE ARTISTAS🎶')
        print('=' * 40)
        print('1️⃣ Agregar Artista')
        print('2️⃣ Consultar Artistas')
        print('3️⃣ Reporte Artista')
        print('4️⃣ Modificar Artista')
        print('5️⃣ Eliminar Artista')
        print('6️⃣ Salir')
        print('=' * 40)

        prompt = input('Selecciona una opción: ').strip()

        if prompt.isnumeric():
            option = int(prompt)
            if option > 0 and option <= 6:
                match option:
                    case 1:
                        limpiar_pantalla()                        
                        add_artist()
                    case 2:
                        limpiar_pantalla()                        
                        show_all_artists()
                    case 3:  
                        limpiar_pantalla()                        
                        show_artist_by_id()
                    case 4:
                        limpiar_pantalla()
                        update_artist()
                    case 5:
                        limpiar_pantalla()                        
                        delete_artist()
                    case 6:
                        bandera=False
            else:
                limpiar_pantalla()
                print('\t Opción no válida, intente de nuevo: ')    
        else:
            limpiar_pantalla()
            print('\t Opción no válida, intente de nuevo: ')