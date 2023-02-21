def validate_username(username):
    # return len(username) > 5
    if len(username) <= 5:
        raise Exception('El username debe poseer una longitud mayor a 5 caracteres')

    return True

try:
    username = 'cody'
    result = validate_username(username)

    print(result)

except Exception as error:
    print('No fue posible completar la operación')
    print(error)