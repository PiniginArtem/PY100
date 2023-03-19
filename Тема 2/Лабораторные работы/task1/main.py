list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]

list_of_unique_values = set(list_)
sum_of_unique_values = sum(list_of_unique_values)
number_of_unique_values = len(list_of_unique_values)
average_of_unique_values = sum_of_unique_values / number_of_unique_values

# print(list_of_unique_values)
print("Сумма уникальных чисел = ", sum_of_unique_values)
print("Количество уникальных чисел = ", number_of_unique_values)
print("Среднее арифметическое уникальных чисел = ", round(average_of_unique_values, 5))