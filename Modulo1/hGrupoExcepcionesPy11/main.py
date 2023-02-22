#ExceptionGroup sólo está disponible en Python 3.11 y superiores

from exceptions import CustomError1, CustomError2, CustomError3

try:
    raise ExceptionGroup(
        'Un grupo de errores propios.',
        [CustomError1(), CustomError2(), CustomError3()]
    )

# except ExceptionGroup as group: #Listado de excepciones
#     print(group)

except *CustomError1:             #Excepciones específicas
    print('Error de tipo 1')

except *CustomError2:
    print('Error de tipo 2')

except *CustomError3:
    print('Error de tipo 3')
