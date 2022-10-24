money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
money_capital = money_capital + salary - spend # остаток после 1-го месяца
month += 1
while money_capital > spend: # пока подушка>трат выполняется цикл
    spend = spend * (increase + 1)
    money_capital = money_capital + salary - spend
    month = month + 1
# TODO Оформить решение

print(month)
