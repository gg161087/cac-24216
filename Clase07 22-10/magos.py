magos = ['alicia', 'david', 'caro']

for mago in magos:
    print(mago.title())

i = 0
while i < len(magos):
    print(magos[i].title())
    i += 1

for valor in range(0, len(magos)):
    print(magos[valor])

magos = ['alicia', 'david', 'caro', 'roberto', 'tusam']
print(magos)
print(magos[0:3])   #Corta desde el indice 0, 3 elementos
print(magos[:2])    #al no indicar el primer valor, empieza desde el primer valor
print(magos[3:])    #al no indicar el segundo valor, es desde el 3er elemento hasta el final