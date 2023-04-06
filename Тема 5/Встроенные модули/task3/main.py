from random import randint


start = -100
stop = 100
count = 50
random_list = [randint(start, stop) for i in range(count)]

count_negative_number = len([negative_number for negative_number in random_list if negative_number < 0])
print(count_negative_number)