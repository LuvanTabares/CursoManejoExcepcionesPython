number1 = 10 #2 variables
number2 = 0
numbers = [0, 1, 2, 3, 4, 5] #----> Generará un error si nos salimos del index

try:
    result = numbers[0] / numbers[10] #**** variable no definida ----> NameError

except ZeroDivisionError as error:
    print('El resultado de la operación tiende a infinito')
    print(error)

except NameError as error:
    print('Variable no definida')
    print(error)

except IndexError as error:
    print('No es posible acceder a dicho índice')
    print(error)

else:
    print('El resultado de la operación es: ', result)

finally:
    print('El programa ha finalizado')

# Pueden surgir errores como en leer un archivo, conectarse a una base de datos, consumir una api

# Se pueden agregar múltiples except para manejar múltiples errores