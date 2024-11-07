# Lista para almacenar las ventas diarias
ventas_por_dia = []

# Registro de ventas por 5 días
dias = 5
contador_dias = 1

while contador_dias <= dias:
    venta_dia = input(f"Ingresá el monto de las ventas para el día {contador_dias}: ")
    
    # Validación de que el monto sea un número positivo
    try:
        venta_dia = float(venta_dia)
        if venta_dia > 0:
            ventas_por_dia.append(venta_dia)
            contador_dias += 1
        else:
            print("El monto debe ser un valor positivo. Intentalo nuevamente.")
    except ValueError:
        print("Por favor, ingresá un número válido.")

# Mostrar ventas diarias
print("\nResumen de ventas diarias:")
for i, venta in enumerate(ventas_por_dia, start=1):
    print(f"Día {i}: ${venta:.2f}")

# Calcular y mostrar el total de ventas y el promedio
total_ventas = sum(ventas_por_dia)
promedio_ventas = total_ventas / dias

print(f"\nTotal de ventas en los 5 días: ${total_ventas:.2f}")
print(f"Promedio de ventas diarias: ${promedio_ventas:.2f}")
