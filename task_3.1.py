def delete(list_, index=None):

    for i in range(-len(list_), len(list_)):
        if index == i:
            del(list_[i])
    if index == None or abs(index) > len(list_) : # abs - модуль
        del (list_[-1])
    return list_
    # TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4],index=51))  # [0, 1, 2, 3] #  index = 51 вставлен для проверки условия с модулем в цикле
