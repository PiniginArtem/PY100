money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while money_capital > 0:
    if money_capital > spend - salary:
        month += 1
        money_capital = round(money_capital - spend + salary, 2)
        # print('После', month, 'месяца в финансовой подушке останется:', money_capital)
        spend = round(spend + spend * increase, 2)
    else:
        money_capital = round(money_capital - spend + salary, 2)
        # print('На', month + 1, 'месяц в финансовой подушке будет недостаточно средств, а именно:', money_capital)

print(month)
