
import re


def login_validation(login: str):
    """
    Login validation function.

    :param login: Login in str format.
    :return: True or False.
    """

    regular = '^[a-zA-Z0-9]{2,10}$'

    matches = re.finditer(regular, login)

    for _ in matches:
        return True
    return False


if __name__ == "__main__":
    print(login_validation('Allosdadww'))  # True
    print(login_validation('66816xasxa'))  # True
    print(login_validation('a6a5xa86xa'))  # True
    print(login_validation('rtbkn16d51'))  # True
    print(login_validation('wiu6ax168a'))  # True
    print(login_validation('wiu6ax168aacaca'))  # False
    print(login_validation('-aaxaidjnmqwjkwn'))  # False