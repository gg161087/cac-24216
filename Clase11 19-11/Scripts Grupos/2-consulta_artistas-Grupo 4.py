# Crear una lista de diccionarios con los datos de los artistas
# 2 - CONSULTAR ARTISTAS


artistas = {
    1: {"nombre": "Taylor Swift", "género": "Pop", "país": "Estados Unidos"},
    2: {"nombre": "Shakira", "género": "Pop", "país": "Colombia"},
    3: {"nombre": "Bad Bunny", "género": "Reguetón", "país": "Puerto Rico"},
    4: {"nombre": "Adele", "género": "Soul", "país": "Reino Unido"},
    5: {"nombre": "Rosalía", "género": "Flamenco", "país": "España"},
}

def buscar_artista(codigo, diccionario):
    bandera=0
    for clave, valor in diccionario.items(): #for k, v in user.items() - for key, value in user.items()
        if clave == codigo:
            bandera=1
            print("Artista encontrado:")
            for k, v in valor.items():
                print(f"{k} : {v}")
    if bandera==0:
        print("No se encontro artista")

codigo= (input("Ingrese codigo del artista a consultar: "))
while not codigo.isdigit():
    codigo= (input("Error, Ingrese codigo del artista a consultar: "))
codigo=int(codigo)
buscar_artista(codigo,artistas)