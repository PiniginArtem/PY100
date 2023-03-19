# TODO продолжить заполнение словаря
dict_hex = {
    '0x0': 0,
    '0x1': 1,
    '0x2': 2,
    '0x3': 3,
    '0x4': 4,
    '0x5': 5,
    '0x6': 6,
    '0x7': 7,
    '0x8': 8,
    '0x9': 9,
    '0xA': 10,
    '0xB': 11,
    '0xC': 12,
    '0xD': 13,
    '0xE': 14,
    '0xF': 15,
    '0x10': 16,
    '0x11': 17,
}

dict_hex_2 = {}
length_dictionary = 18      # количество элементов в словаре
for x in range(length_dictionary):      # пробегаем от 0-ого элемента до конца словаря
    key_dictionary = str(hex(x))        # ключ словаря
    if key_dictionary[2:].isdigit():        # проверяем отсутсвуют ли буквы в записи 16-ого числа
        dict_hex_2[key_dictionary] = x              # записываем значение словаря
    else:
        key_dictionary = key_dictionary[:2] + key_dictionary[2:].upper() # если есть буквы, приводим к верхнему регистру
        dict_hex_2[key_dictionary] = x              # записываем значение словаря с исправленным ключом

print(dict_hex)
print(dict_hex_2)
