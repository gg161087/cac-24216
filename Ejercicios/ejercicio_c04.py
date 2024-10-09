'''
Ticket de la compra
1. Escribir un programa que solicite el nombre, la 
cantidad y el valor unitario de tres productos.
2. Luego, debe calcular el importe de IVA (21%) de 
cada producto.
3. Por último, debe mostrar en la terminal el ticket de 
la operación con todos los datos de la compra. 

Consumo de combustible
Realizar una aplicación en Python que;
A partir de la cantidad de litros de combustible que 
consume un coche por cada 100 km de recorrido, el 
costo de cada litro de combustible y la longitud del 
viaje realizado (en kilómetros), muestra un detalle de 
los litros consumidos y el dinero gastado.
'''
#Ticket de la compra
IVA = 0.21

def calcular_iva(precio):
    return precio * IVA

def precio_con_iva(precio):
    return precio * (1 + IVA)

nombre_producto1 = input('Ingrese el nombre del producto 1: ')
cantidad_producto1 = int(input('Ingrese la cantidad del producto 1: '))
valor_unitario_producto1 = float(input('Ingrese el valor unitario del producto1: '))

nombre_producto2 = input('Ingrese el nombre del producto 2: ')
cantidad_producto2 = int(input('Ingrese la cantidad del producto 2: '))
valor_unitario_producto2 = float(input('Ingrese el valor unitario del producto2: '))

nombre_producto3 = input('Ingrese el nombre del producto 3: ')
cantidad_producto3 = int(input('Ingrese la cantidad del producto 3: '))
valor_unitario_producto3 = float(input('Ingrese el valor unitario del producto3: '))

importe_producto1 = cantidad_producto1 * valor_unitario_producto1
importe_producto2 = cantidad_producto2 * valor_unitario_producto2
importe_producto3 = cantidad_producto3 * valor_unitario_producto3

iva_producto1 = importe_producto1 * IVA
iva_producto2 = importe_producto2 * IVA
iva_producto3 = importe_producto3 * IVA

total_producto1 = importe_producto1 + iva_producto1
total_producto2 = importe_producto2 + iva_producto2
total_producto3 = importe_producto3 + iva_producto3

total_sin_iva = importe_producto1 + importe_producto2 + importe_producto3
total_iva = iva_producto1 + iva_producto2 + iva_producto3
print('')
print('-' * 50)
print('Ticket de la compra'.center(50))
print('-' * 50)
print(f'{"Producto":<15} {"Canti.":<5} {"P.U.($)":<10} {"Total($)":<10} {"IVA($)":<10}')
print("-"*50)
print(f"{nombre_producto1:<15} {cantidad_producto1:>5} {valor_unitario_producto1:>10.2f} {total_producto1:>10.2f} {iva_producto1:>10.2f}")
print(f"{nombre_producto2:<15} {cantidad_producto2:>5} {valor_unitario_producto2:>10.2f} {total_producto2:>10.2f} {iva_producto2:>10.2f}")
print(f"{nombre_producto3:<15} {cantidad_producto3:>5} {valor_unitario_producto3:>10.2f} {total_producto3:>10.2f} {iva_producto3:>10.2f}")
print("-"*50)
print(f"{'Total Compra sin IVA:':<30} ${total_sin_iva:>10.2f}")
print(f"{'Total IVA:':<30} ${total_iva:>10.2f}")
print(f"{'TOTAL:':<30} ${total_sin_iva + total_iva:>10.2f}")
print("-"*50)
print("Gracias por su compra. ¡Vuelva pronto!")
print("-"*50)
print('')
#Consumo de combustible