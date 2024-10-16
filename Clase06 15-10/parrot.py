#parrot

prompt = '\n Dime algo y lo repito'
prompt += '\n Ingrese la palabra "salir" para finalizar: '

message = '' #forzar a que al menos 

while message != 'salir':
    message = input(prompt)
    if message != 'salir':
        print(message)