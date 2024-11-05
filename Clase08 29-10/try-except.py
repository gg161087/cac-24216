'''
En Python, cuando usas try/except, puedes agregar else y/o finally para controlar mejor el flujo de ejecución después de intentar ejecutar el código dentro de try. 
La cláusula else se ejecuta solo si no ocurrió ninguna excepción en el bloque try. Si se lanza una excepción, else se omite.
Útil para: Código que solo debería ejecutarse cuando try se completa correctamente, y que depende de que try no falle.
'''
try:
    # Código que podría lanzar una excepción
    result = 10 / 2
except ZeroDivisionError:
    # Manejo de excepción si ocurre una división por cero
    print("Error: división por cero.")
else:
    # Se ejecuta solo si no hubo excepciones en try
    print("El resultado es:", result)
    
'''
En este ejemplo, si no ocurre una división por cero, se imprime el resultado; si ocurre, else no se ejecutará.
La cláusula finally se ejecuta siempre, independientemente de si hubo o no una excepción. Se usa generalmente para tareas de limpieza, 
como cerrar archivos o conexiones, que deben ejecutarse sin importar si el código falló o no.
Útil para: Código que siempre debe ejecutarse, como la liberación de recursos o la ejecución de acciones finales necesarias.
'''
try:
    # Código que podría lanzar una excepción
    result = 10 / 0
except ZeroDivisionError:
    # Manejo de excepción si ocurre una división por cero
    print("Error: división por cero.")
finally:
    # Siempre se ejecuta
    print("Este mensaje se imprime sin importar si hubo o no un error.")
'''
Aquí, aunque ocurra una excepción de división por cero, el mensaje en finally se imprime siempre.
En resumen
else se ejecuta solo si no hubo excepciones.
finally se ejecuta siempre, tanto si hubo excepciones como si no.
Ambos bloques pueden usarse juntos para combinar lógica de ejecución condicional con tareas de limpieza necesarias.
'''