'''
EJERCICIO 1 - OPERACIONES BASICAS
1- Crea un programa que solicite al usuario dos
números enteros.

2- Realiza las siguientes operaciones: suma,
resta, multiplicación, y módulo.

3- Muestra el resultado de cada operación en un
formato claro y amigable.

Asegúrate de incluir mensajes personalizados que
expliquen cada resultado, por ejemplo: "La suma
de tus números es: X".
'''

num1 = int(input("ingrese un número entero y presione enter: "))
num2 = int(input("ingrese otro número entero y presione enter: "))
suma = num1 + num2
resta = num1 - num2
mult =  num1 * num2
div = num1 / num2
div = f"{div:.2f}"
print()
print(50*"-")
print()
print("La suma de", num1,  "y", num2,  "da como resultado:", suma)
print()
print("La resta de", num1,  "y", num2,  "da como resultado:", resta)
print()
print("La división de", num1,  "y", num2,  "da como resultado:", div)
print()
print("La multiplicación de", num1,  "y", num2,  "da como resultado:", mult)
print()
print(50*"-")