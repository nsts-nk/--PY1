def get_random_password() -> str:# TODO написать функцию генерации случайных паролей
    import random
    n=8
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return str(random.sample(alphabet, n))


print(get_random_password())
