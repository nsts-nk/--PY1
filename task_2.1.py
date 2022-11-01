def get_count_char(str_):
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    lower_str = str_.lower()
    s_dict = {} # создание словаря
    count = 0 # кол-во символов
    for symbol in lower_str:
        if symbol.isalpha():
            s_dict[symbol] = s_dict.get(symbol, count) + 1
    return s_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

def get_percentage_char(str_):
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    lower_str = str_.lower()
    s_dict = {} # создание словаря
    percentage = 0 # процент по отношению ко всем символам
    for symbol in lower_str:
        if symbol.isalpha():
            s_dict[symbol] = s_dict.get(symbol, percentage) + 1/len(lower_str) * 100

    return s_dict

print(get_count_char(main_str))
print(get_percentage_char(main_str))
