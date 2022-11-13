# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
list_of_dicts = [] # пустой список

for a in range(16):
    dict = {"dec": a, "bin": bin(a), "oct": oct(a), "hex": hex(a)} # перевод в системы
    list_of_dicts.append(dict)

pprint(list_of_dicts)