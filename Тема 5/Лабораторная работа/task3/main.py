from random import sample
def get_unique_list_numbers() -> list[int]:
    """
    функция, которая возвращает список, заполненный случайными уникальными целыми числами
    :return: list[int]
    """
    return sample(range(-10, 11), k=15)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
