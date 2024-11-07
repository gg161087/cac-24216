alien = {'color': 'amarillo', 'puntaje': 5, 'posicion_x': 0, 'posicion_y': 25, "velocidad": 'media'}
#lento - inncremento x = 1
#media - incremento x = 3
#rapido - incremento x = 5

if alien['velocidad'] == 'lento':
    incremento_x = 1
elif alien['velocidad'] == 'media': 
    incremento_x = 3
else:
    incremento_x = 5
    
alien['posicion_x'] += incremento_x

print(f"La nueva posición del alien es {alien['posicion_x']}")
print(alien)