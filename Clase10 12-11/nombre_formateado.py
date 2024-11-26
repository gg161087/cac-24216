#funciones con retorno de valor
# retorna un dato simple
def obtener_nombre_formateado(nombre, apellido):
    """retorna el nombre completo del user"""
    nombre_completo = nombre + ' '+apellido
    return nombre_completo.title()

#invocar - main
print(obtener_nombre_formateado('josé','perez'))
full_name = obtener_nombre_formateado('maría', 'sosa')
print(full_name)
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print(obtener_nombre_formateado(nombre, apellido))

