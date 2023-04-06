from random import choices
from collections import Counter

EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

for count in counts:
    list_value = choices(coin, k=count)
    list_count = Counter(list_value)

    if list_count[EAGLE] > list_count[TAILS]:
        list_freq.append(list_count[TAILS] / list_count[EAGLE])
    else:
        list_freq.append(list_count[EAGLE] / list_count[TAILS])

print(list_freq)
