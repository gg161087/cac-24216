productos = {1:{'nombre':"the beatles",'genero':'rock'},2:{'nombre':"rolling",'genero':'heavy'},3:{'nombre':"rolling",'genero':'heavy'}}

def eliminarArtista():
    while True:
        try:
            print(productos)
            id = int(input("Escriba el número de ID para eliminar un artista: "))
            del(productos[id])
            print(productos)
            break
        except ValueError:
            print("  Por favor ingrese un valor numerico")
    
eliminarArtista()    