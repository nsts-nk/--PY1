2
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
s_dict0 = {}
count0 = 0
symbols = len(main_str)
lower_str = main_str.lower()
for symbol in lower_str:
    s_dict0[symbol] = s_dict0.get(symbol, count0) + 1
    # создали словарь, в котором посчитано количество каждого символа, не только буквы  (пункт 1 задания)

def get_percentage_char(s_dict0): # функция принимает словарь, в котором были посчитаны все символы
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    s_percentage_dict = {} # создание словаря
    percentage = 0 # процент по отношению ко всем символам
    for symbol in lower_str:
        s_percentage_dict[symbol] = s_percentage_dict.get(symbol, percentage) + 1/len(lower_str) * 100

    return s_percentage_dict

print(s_dict0)
print(get_count_char(main_str))
print(get_percentage_char(main_str))
