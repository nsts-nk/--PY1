import random


def get_unique_list_numbers() -> list[int]:# TODO написать функцию для получения списка уникальных целых чисел

    from random import randint
    count_of_unique_numbers = 0
    list_of_unique_numbers = []
    while count_of_unique_numbers < 15:
        numbers = random.randrange(-10, 10)

        if numbers not in list_of_unique_numbers:
            list_of_unique_numbers.append(numbers)
            count_of_unique_numbers +=1
    return list_of_unique_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
