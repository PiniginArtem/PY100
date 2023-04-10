# def remove(list_: list, value_: any) -> list:
#     list_def = list_[:]
#     i = 0
#     while True:
#         if list_def[i] != value_:
#             i += 1
#         else:
#             del list_def[i]
#         if i == len(list_def):
#             break
#     if len(list_def) == len(list_):
#         raise ValueError(f"В этом списке нет элемента {value_}")
#     return list_def

def remove(list_: list, value_: any) -> list:
    list_def = list_[:]
    for i in range(len(list_def)):
        if list_def[i] == value_:
            del list_def[i]
            return list_def
    raise ValueError(f"В этом списке нет элемента {value_}")


print(remove([0, 0, 1, 2], 0))  # [0, 1]
print(remove([0, 1, 1, 2, 3], 1))  # [0, 1, 2, 3]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
