# def delete_index_and_last(list_, index=None): # функция которая удаляет значения по индексу и последнее
#     if index is None:
#         return list_[:-2] # если индекс не задан, то удаляет 2 последних значения
#     elif type(index) == int:
#         return list_[:index] + list_[index + 1:-1] # удаляет значение по индексу и последние значение
#     else:
#         print("индекс должен быть типа int") # не правильно задан индекс
#         return

def delete(list_, index=None): # функция которая удаляет значение по индексу
    if index is None:
        return list_[:-1] # если индекс не задан, то удаляет последние значение
    elif type(index) == int:
        return list_[:index] + list_[index + 1:] # удаляет значение по индексу
    else:
        print("индекс должен быть типа int")
        return

if __name__ == '__main__':
    print(delete([0, 0, 1, 2], index=0))  # [0, 1]
    print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
    print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
