#Operaciones básicas
print('Ingrese dos números enteros \n')
numero_01 = int(input('Ingrese el primer: '))
numero_02 = int(input('Ingrese el segundo: '))

suma = numero_01 + numero_02
resta = numero_01 - numero_02
multi = numero_01 * numero_02
modulo = numero_01 % numero_02

print(f'La suma de tus números es: {suma}')
print(f'La resta de tus números es: {resta}')
print(f'La multiplicación de tus números es: {multi}')
print(f'El módulo de tus números es: {modulo}')

#Calculadora de propinas
print('Calculadora de propinas \n')
monto_total = float(input('Ingresa el monto total de la cuenta: '))
porcentaje_propina = float(input('Ingresa el porcentaje de propina que deseas dejar (por ejemplo, 15 para 15%): '))
propina = (porcentaje_propina / 100) * monto_total
total_pagar = monto_total + propina
print(f'\nMonto total de la cuenta: ${monto_total:.2f}')
print(f'Propina ({porcentaje_propina}%): ${propina:.2f}')
print(f'Total a pagar: ${total_pagar:.2f}')