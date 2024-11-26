def mostrar_reporte(artistas):
    if not artistas:
        print('No hay artistas registrados')
    else:
        print('Reporte de artistas registrados:')
        for nombre, info in artistas.items():
            print(f'\nNombre: {nombre}')
            print(f'Género: {info["genero"]}')
            print(f'Año de registro: {info["año de registro"]}')