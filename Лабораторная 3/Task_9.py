salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев

total_spend = 6000 # траты за 1 месяц

# TODO Оформить решение

for i in range(months - 1): # не берём в расчёт проценты в 1 месяц
    spend = spend * (increase + 1) # траты на каждый месяц
    total_spend += spend # общие траты

need_money = total_spend - salary * 10


print(round(need_money))
