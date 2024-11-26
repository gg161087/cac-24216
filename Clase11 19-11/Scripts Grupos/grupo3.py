almacenamiento = []
contador = 0
flag = True

while flag:
  try:
    nombre = input('Ingrese el nombre del artista: ')
    genero = input('Ingrese el estilo musical del artista: ')
    edad = int(input('Ingrese la edad del artista: '))
    productora = input('Ingrese la productora a la cual pertenece el artista: ')
    contador = contador + 1
    artista = {
        'Nombre' : nombre,
        'Genero' : genero,
        'Edad' : edad,
        'Productora' : productora,
        'Id' : contador
    }
    almacenamiento.append(artista)
    nuevo_ingreso = input('Deseas ingresar un nuevo artista (y/n): ')
    if nuevo_ingreso == 'n' or nuevo_ingreso == 'N':
      flag = False
    elif nuevo_ingreso == 'y' or nuevo_ingreso == 'Y':
      Flag = True
  except ValueError:
    print("Ingreso un dato en un formato erroneo, intente nuevamente")