list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_number = list_numbers[0]  # пусть значение первого элемента будет самым высоким

for current_number in list_numbers:  # перебираем каждый элемент
    if current_number > max_number:  # если текущий элемент больше того, который встречали ранее
        max_number = current_number  # то перезаписываем элемент с максимальным значением

max_index = list_numbers.index(max_number) # находим индекс максимального элемента

list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index] # меняем местами макс и последние элементы


# TODO Оформить решение

print(list_numbers)
