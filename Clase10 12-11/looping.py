user = {
    'nombre' : 'fernando',
    'apellido' : 'lopez',
    'username' : 'flopez' 
}

#acceder a la pareja clave valor
for clave, valor in user.items(): #for k, v in user.items() - for key, value in user.items()
    print("Clave: ", clave)
    print("Valor: ", valor)
    
#acceder a las claves
lenguajes_favoritos = {
    'juana' : 'c',
    'guille' : 'php',
    'pedro': 'python',
    'maria': 'java'
}
for clave in lenguajes_favoritos.keys():
    print("Nombre: ", clave)
    
#acceder a los valores
for valor in lenguajes_favoritos.values():
    print(valor)
    
amigos = ['luis', 'juana', 'maria']
for nombre in lenguajes_favoritos.keys():
    print(nombre)
    if nombre in amigos:
        print(f"{nombre.title()} respondió la encuesta y su respuesta fue {lenguajes_favoritos[nombre].upper()}")
        
#ordenar a traves de la clave
print('ordenar')
for nombre in sorted(lenguajes_favoritos.keys()):
    print(nombre)      
    
#lista como valor
lenguajes_favoritos = {
    'juana' : ['c', 'php'],
    'guille' : ['php'],
    'pedro': ['python', 'javascript'],
    'maria': ['java']
}


pizzas = {
    'tamaño' : 12,
    'ingredientes': ['aceitunas', 'jamon', 'morrones', 'mozarella']
}