#----> OOP ----> Herencia -> Exception -> BaseException


try:
    numbers = [0, 1, 2, 3, 4, 5]  #----> Generará un error si nos salimos del index

    number1 = numbers[0] #2 variables
    number2 = numbers[4]

    result = number1 / number2 #**** variable no definida ----> NameError

except Exception as error:
    print('No fue posible realizar la operación')
    print(error)

else:
    print('El resultado de la operación es: ', result)

finally:
    print('El programa ha finalizado')

# Pueden surgir errores como en leer un archivo, conectarse a una base de datos, consumir una api

# Se pueden agregar múltiples except para manejar múltiples errores