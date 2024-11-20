artistas = [
    {
        'codigo': 1,
        'artista': 'The Beatles',
        'genero': 'rock',
    },
    {
        'id': 2,
        'artista': 'Adele',
        'genero': 'pop'
    }
]

def listar_artitas():    
    if not artistas:
        print('La lista de artistas está vacía.')
    else:
        print(f'{"#":<5} {"Artista":<15} {"Genero":>15}')
        for artista in artistas:
            print(f"{artista['codigo']:<5} {artista['artista']:<15} {artista['genero']:>15}")

def listar_por_genero(genero):
    if not artistas:
        print('La lista de artistas está vacía.')
    else:        
        for artista in artistas:
            if artista['genero'] == genero:
                print(f'{"#":<5} {"Artista":<15} {"Genero":>15}') 
                print(f"{artista['codigo']:<5} {artista['artista']:<15} {artista['genero']:>15}")

def filtrar(opcion, prompt):
    bandera = ''    
    if opcion == '1':
        bandera = 'codigo'
    elif opcion == '2':
        bandera = 'artista'
    else:
        bandeta = 'genero'
    if not artistas:
        print('La lista de artistas está vacía.')
    else:        
        for artista in artistas:
            if artista[bandera] == prompt:
                print(f'{"#":<5} {"Artista":<15} {"Genero":>15}') 
                print(f"{artista['codigo']:<5} {artista['artista']:<15} {artista['genero']:>15}")


