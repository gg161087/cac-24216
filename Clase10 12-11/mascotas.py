#mascotas.py

def describir_mascota(tipo_animal, nombre_mascota):
    """Describir la mascota"""
    print(f"Tengo un {tipo_animal}.")
    print(f"Y su nombre es {nombre_mascota.title()}")
    
#invocar múltiple
#argumentos posicionales
describir_mascota('gato', 'ruby')
describir_mascota('perro', 'sheena')
describir_mascota('gallo', 'enzo')
#argumentos palabras clave
describir_mascota(nombre_mascota='json', tipo_animal='gato')

