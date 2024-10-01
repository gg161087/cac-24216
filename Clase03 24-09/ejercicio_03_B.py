'''
EJERCICIO 2 - CALCULADORA DE PROPINAS
Escribe un programa en Python que calcule la
propina que se debe dejar en un restaurante.

El script debe solicitar al usuario el monto total de
la cuenta y el porcentaje de propina que desea
dejar.

Utilizando operadores aritméticos, calcula la
cantidad de propina y el total a pagar (incluyendo
la propina).

Finalmente, muestra los resultados en la pantalla.
'''
print()
print(60*"*")
print()
print()
print(40*"=")
print("|       CALCULADORA DE PROPINAS        |")
print(40*"=")
print("|   INGRESE EL IMPORTE DE LA CUENTA    |")
print("|        Y PRESIONE ENTER              |")
print(40*"=")
cuenta = float(input("$ "))
print(40*"=")
print("|   INGRESE EL PORCENTAJE DE PROPINA   |")
print("|        Y PRESIONE ENTER              |")
print(40*"=")
porcent = int(input("% "))
propina = (cuenta / 100) * porcent
total = cuenta + propina
print()
print()
print("EL MONTO DE LA PROPINA ES DE $", propina)
print()
print("EL IMPORTE A ABONAR CON LA PROPINA ES DE $", total)
print()
print()