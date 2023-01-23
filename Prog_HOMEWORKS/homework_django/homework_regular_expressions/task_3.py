
import re


def email_checker(email: str):
    """
    Check e-mail address for conformity.

    :param email: E-mail in str format.
    :return: True or False.
    """

    regular = r"^[a-zA-Z0-9]{1}[a-zA-Z0-9_]+(-{1})?[a-zA-Z0-9_]+@{1}([a-zA-Z0-9]+\.)+[a-z0-9]{1}([a-z0-9-]*[a-z0-9])?$"

    matches = re.finditer(regular, email)

    for _ in matches:
        return True
    return False


if __name__ == "__main__":
    print(email_checker('wolimmozuma-7567@yopmail.com'))  # True
    print(email_checker('wolimmozuma-7567@yop-mail.com'))  # False (yop-mail)
    print(email_checker('wolimmozuma--7567@yopmail.com'))  # False (wolimmozuma--7567)
    print(email_checker('-wolimmozuma-7567@yopmail.com'))  # False (-wolimmozuma)
    print(email_checker('woli'))  # False (woli)