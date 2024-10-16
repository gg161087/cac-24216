mensaje = "I love Python"
print(mensaje[5]) #accedo item

#por elemento
for letra in mensaje:
    print(letra)
    
#por posicion
contador = 0
while contador < len(mensaje):
    print(mensaje[contador])
    contador+=1
    
#por elemento
numeros = [8, 10, 7] #lista
for numero in numeros:
    print(numero)