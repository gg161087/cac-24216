#Listas
motos = ['fencor', 'zanella', 'scooter', 'motomel', 'honda']
print('Lista: ')
print(motos)

#Modificar el primer elemento de la lista
print('Modificar el primer elemento de la lista: motos[0] = "duke"')
motos[0] = 'duke'
print(motos)

#Agregar un elemento mas a lo ultimo de la lista
print('Agregar un elemento mas a lo ultimo de la lista: motos.append("fencor")')
motos.append('fencor')
print(motos)
'''
nueva_moto = input('Ingrese nuevo modelo: ') #Falta validar 
motos.append(nueva_moto)
print(motos)
'''

#Insertar dentro de la lista en la posicion 0
print('Insertar dentro de la lista en la posicion 0: motos.insert(0, "suzuki")')
motos.insert(0, 'suzuki')
print(motos)

#Eliminar 
print('Eliminar con del: del motos[3]')
del motos[3]
print(motos)
print('Eliminar por indice y se puede guardar el valor eliminado: eliminada = motos.pop(0)')
eliminada = motos.pop(0)#Eliminar por indice y se puede guardar el valor eliminado
'''Si no le paso un argumento elimina el ultimo'''
print(motos)
print(eliminada)
print('Eliminar por valor: motos.remove("motomel")')
motos.remove('motomel')#Eliminar por valor
print(motos)