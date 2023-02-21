number1 = 10 #2 variables
number2 = 0

try:

    result = number1 / number2 #Operación/Esta línea arrojará una excepción ----> ZeroDivisionError

    print('El resultado de la operación es: ', result) #los print no aparecen por la terminación abrupta del código

    print('El programa ha finalizado')

except ZeroDivisionError as error:

    print('El resultado de la operación tiende a infinito')
    print(error)

# Pueden surgir errores como en leer un archivo, conectarse a una base de datos, consumir una api