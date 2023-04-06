from random import sample
from string import ascii_letters, digits


def get_random_password(n: int = 8) -> str:
    """
    Функция для генерации случайных паролей, используются A - Z, a - z, 0 - 9
    :param n: int - длина пароля
    :return: str - случайный пароль
    """
    return ''.join(sample(ascii_letters + digits, n))


print(get_random_password())
