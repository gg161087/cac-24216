#entrada
# Guardar los ingresos de los primeros 6 meses en variables 
ingreso_enero = 1500 
ingreso_febrero = 1600 
ingreso_marzo = 1700 
ingreso_abril = 18000 
ingreso_mayo = 19500 
ingreso_junio = 2000 

#proceso
# Calcular el promedio de los ingresos 
sumatoria = ingreso_enero + ingreso_febrero + ingreso_marzo + ingreso_abril + ingreso_mayo + ingreso_junio #creo una variable auxiliar
promedio_ingresos = sumatoria / 6 #float

#promedio_ingresos = (ingreso_enero + ingreso_febrero + ingreso_marzo + ingreso_abril + ingreso_mayo + ingreso_junio) / 6 

#salida
# Mostrar el promedio con una leyenda 
# string - concatenar
print("El ingreso promedio en el semestre es de ", promedio_ingresos)
print("El ingreso promedio en el semestre es de "+ str(promedio_ingresos))#conversión de datos float->str 
# format string
print(f"El ingreso promedio en el semestre es de {promedio_ingresos:.2f}") #3.6
print("El ingreso promedio en el semestre es de {}".format(promedio_ingresos))#no permite calculos dentro de {}


#------------------------------------------------------


#conversion.py
#int -> str
comision = 24216 #int
print("Bienvenidos"+" "+"comision "+str(comision))

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

print(f"Su IMC es: {imc:.2f}")

#------------------------------------------------------
#operaciones aritmeticas
# 1. parentesis
# 2. potencia, raices
# 3. division, multiplicacion, modulo o resto
# 4. suma y resta


#operadores relacionales -> arrojan valor booleano
edad1 = 25
print(edad1 >= 18) #True
edad2 = 10
#<
menor_edad = edad2 < 18 #true
print(menor_edad)
#>
#>=
#<
#<=
print("cola" == "Cola") #false
print(4 != 0) #True #distinto

#operadores logicos
# y (and) o (or) no(not)
print( 3 > 4 and "hola" == "hola")
#       F           V = F

#leo requisitos para cursar
edad = 19
residencia = "caba"
titulo_secundario = False #asignar 

#evaluo si permite ingresar
print(edad >= 18 and (residencia == "caba" or residencia == "amba") and titulo_secundario == True)

#pertenencia
#in - not in
# mensaje = "I love Python"
# respuesta = "Python" in mensaje
# print(respuesta)
# respuesta = "Java" in mensaje
# print(respuesta)

#------------------------------------------------------

'''
Repaso de la clase 2
24/09/2024
'''
#instrucción print
print("Bienvenidos!") #escribir - imprimir 
print('Esto es Python',end="-")
print("Comisión: #24216")

# variables
# identificadores - nombre de variable
# asignación  declaración definición actualización
nombre = "Carlos" #str
apellido = "Lopez" #str
#apellido = 42 #int
edad = 42 #int
estatura = 1.78 #float 
cliente_premium = False #bool
tipoCliente = 'VIP'
realizaActividadFisica = True
estado_civil = None #not defineds

#función type()
print(type(estado_civil)) #bool



# Guardar los ingresos de los primeros 6 meses en variables 
ingreso_enero = 1500 
ingreso_febrero = 1600 
ingreso_marzo = 1700 
ingreso_abril = 1800 
ingreso_mayo = 1900 
ingreso_junio = 2000 
# Calcular el promedio de los ingresos 
sumatoria = ingreso_enero + ingreso_febrero + ingreso_marzo + ingreso_abril + ingreso_mayo + ingreso_junio #creo una variable auxiliar
promedio_ingresos = sumatoria / 6 #float

#promedio_ingresos = (ingreso_enero + ingreso_febrero + ingreso_marzo + ingreso_abril + ingreso_mayo + ingreso_junio) / 6 

# Mostrar el promedio con una leyenda 
# string - concatenar
print("El ingreso promedio en el semestre es de ", promedio_ingresos)
print("El ingreso promedio en el semestre es de "+ promedio_ingresos)
print(f"El ingreso promedio en el semestre es de {promedio_ingresos:.2f}")

#------------------------------------------------------

#strings.py

print("Lista de compras:\n")#título y salto de línea
print("1.\t Leche") #alt+92
print("2.\t Aceite")
print("3.\t Azúcar")
print("4.\t Carne")
print("5.\t Arroz")
print()
print("No olvides tu bolsa ecológica!\n")

#concatenar - unir

mensaje = "Bienvenidos"
mensaje += " a Talento Tech" #uniendo cadenas
print(mensaje)

mensaje2 = "Comisión"+" "+" número: 24216" #unir concatenar
print(mensaje2)

comision = 24216 #int
print(mensaje+" "+"comision "+str(comision))






