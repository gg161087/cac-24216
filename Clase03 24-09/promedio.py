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
