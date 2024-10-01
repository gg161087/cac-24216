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