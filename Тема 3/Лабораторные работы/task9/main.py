salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

increase +=1 # добавим 100%, чтоб удобнее было умножать
need_money = 0  # количество денег, чтобы прожить 10 месяцев

for current_month in range(1, months+1):
    need_money += spend - salary
    spend *= increase
print(round(need_money))
