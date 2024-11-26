#funcion con retorno de valor
#retorna un diccionario

def construir_persona(nombre, apellido, edad = ''):
    """Retorna un diccionario con la información de la persona"""
    persona = {'nombre': nombre, 'apellido': apellido}
    if edad:
        persona['edad'] = edad
    return persona

#invocar
musico = construir_persona('jimi', 'hendrix')
conductora = construir_persona('wanda', 'nara', 40)
print(musico)
print(conductora)