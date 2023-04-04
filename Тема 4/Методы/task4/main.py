# TODO реализовать функцию
def insert(list_, value, index=0):
    list_ = list_ + [1]
    for i in range(len(list_) - 1, index, -1):
        list_[i] = list_[i - 1]
    list_[index] = value
    return list_


print(insert([1], value=0))  # [0, 1]
print(insert([0, 2], value=1, index=1))  # [0, 1, 2]
print(insert([0, 1, 2], value=3, index=3))  # [0, 1, 2, 3]
