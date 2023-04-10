# TODO написать функцию index
def index(list_: list, value_: any) -> int:
    for i in range(len(list_)):
        if list_[i] == value_:
            return i
    raise ValueError


list_items = [1, 2, "3", 1]
print(index(list_items, 1) == list_items.index(1))  # True
