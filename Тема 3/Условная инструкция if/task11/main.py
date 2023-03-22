month = 9

spring_months = {3: 'Март',
                 4: 'Апрель',
                 5: 'Май'}  # TODO записать словарь весенних месяцев, где ключ это номер месяца, а значение его название
summer_months = {6: 'Июнь',
                 7: 'Июль',
                 8: 'Август'}  # TODO записать список месяцев лета
autumn_months = {9: 'Сентябрь',
                 10: 'Октябрь',
                 11: 'Ноябрь'}  # TODO записать кортеж месяцев осени
winter_months = {12: 'Декабрь',
                 1: 'Январь',
                 2: 'Февраль'}  # TODO записать список месяцев зимы

if month in spring_months:
    print("Весна")
elif month in summer_months:
    print("Лето")
elif month in autumn_months:
    print("Осень")
elif month in winter_months:
    print("Зима")
# TODO дописать условие elif для осени и зимы
