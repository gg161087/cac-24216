#conversion.py
#int -> str
comision = 24216 #int
print('Bienvenidos'+' '+'comision '+str(comision))

#ingreso por teclado
#entrada
#str -> float
#forma extensa
# estatura =  input("Ingrese su estatura (en metros): ") 
# estatura_float = float(estatura)
#forma abreviada
estatura = float(input("Ingrese su estatura (en metros): "))
peso = float(input("Ingrese su peso (en kg.): "))

#calcular imc
#imc = peso/estatura**2 #potencia 
imc = peso/pow(estatura, 2) #funcion potencia de python

print(f'Su IMC es: {imc:.2f}')
