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









