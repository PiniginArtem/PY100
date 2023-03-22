list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0  #Изначально присваиваем индекс 0ого элемента
max_number = list_numbers[max_index]  #Изначально максимальное число - первый элемент
for index, number in enumerate(list_numbers):  #Перебираем индексы и значения списка
    if number > max_number:  #Сверяем текущий элемент с максимальным, если они равны останется первый максимальный
        max_number = number  #Можно было не записывать переменную, т.к. нужен только индекс
        max_index = index
# print('max_index = ', max_index, 'max_number = ', max_number)
list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]

print(list_numbers)
