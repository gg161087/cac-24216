alien_0 = {
    "color": "verde", 
    "puntaje": 5,
} #diccionario
print(alien_0)

print(alien_0["color"]) #acceder a un valor
print(alien_0["puntaje"])

nuevo_puntaje = alien_0["puntaje"]
print(f"Obtuviste un total de {nuevo_puntaje}")

#agregar nueva pareja clave valor
alien_0['posicion_x'] = 0
alien_0['posicion_y'] = 25
print(alien_0)

#partir de un diccionario vacio
alien_1 = {}
print(alien_1)
alien_1['color'] = "rojo"
alien_1['puntaje'] = 10
print(alien_1)

#actualizar valores
alien_0["color"] = "amarillo"
print(alien_0)