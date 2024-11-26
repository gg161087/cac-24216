#mascotas.py
#valores por default
def describir_mascota(nombre_mascota, nombre_duenio, tipo_animal='perro', edad = 0):
    """Describir la mascota"""
    print(f"Tengo un {tipo_animal}.")
    print(f"Y su nombre es {nombre_mascota.title()}")
    print(f"Dueño: {nombre_duenio}")
    if edad != 0:
        print(f"Tiene {edad} años.")
    
    
#invocar múltiple
#argumentos posicionales
describir_mascota('ruby', 'Rebeca','gato')
describir_mascota('sheena', 'Juan', edad=13)
describir_mascota('enzo', 'David','gallo',1)

#argumentos palabras clave - Invocaciones equivalentes
describir_mascota(tipo_animal='gato', nombre_mascota='json', nombre_duenio='pepe')
describir_mascota('json', 'pepe','gato')
describir_mascota(nombre_duenio='pepe',nombre_mascota='json', tipo_animal='gato')
describir_mascota('json','pepe') #asume el valor por default




