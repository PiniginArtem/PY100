list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

cout_even = 0
cout_odd = 0

for _ in list_:
    if _ % 2 == 0:
        cout_even += 1
    elif _ % 2 == 1:
        cout_odd += 1

if cout_even > cout_odd:
    print("Четных чисел больше")
elif cout_odd > cout_even:
    print("Нечетных чисел больше")
elif cout_odd == cout_even:
    print("Четных и нечетных одинаковое количество")
