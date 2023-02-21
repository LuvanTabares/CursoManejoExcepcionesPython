class UsernameException(Exception):

    def __init__(self, username):
        self.username = username
        self.message = f'El usernmae "{self.username}" no cumple con los requerimientos'

        super().__init__(self.message)


def validate_username(username):
    # return len(username) > 5
    if len(username) <= 5:
        raise UsernameException(username)

    return True

try:
    username = 'aaa'
    result = validate_username(username)

    print(result)

except UsernameException as error:
    print('No fue posible completar la operación')
    print(error)