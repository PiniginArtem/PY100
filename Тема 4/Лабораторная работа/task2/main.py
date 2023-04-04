def get_count_char(str_):
    number_of_letters = {}  # создаём пустой словарь
    for letter in str_.lower():  # пробегаем по каждому символу в строке. Строка приведена к нижнему регистру
        if letter.isalpha():  # проверяем является ли символ буквой
            if letter in number_of_letters.keys():  # проверяем есть буква в словаре
                number_of_letters[letter] += 1  # если есть буква, то увиличиваем кол-во на 1
            else:
                number_of_letters[letter] = 1  # если нет буквы в словаре, то создаем запись буквы
    return number_of_letters


def ratio_symbol_in_str(dict_):
    """
    Функия, которая преобразует количество каждого элемента на процентное отношение ко всем символам.
    На входе должна получить словарь со значениями {буква: количество, буква2: количество}.
    На выходе возвращает словарь со значениями {буква: процентное содержание, буква2: процентное содержание},
    процентное содержание округлено до 2 знака после зяпятой
    """
    if type(dict_) != dict:  # проверяем, является ли входная переменная словарём
        print('Это не словарь!')
        return
    dict_local = dict_.copy()  # копируем глобальный словарь в локальный, чтоб изнчальный словарь не изменился
    for letter in dict_local.keys():  # Пробегаем по каждомой букве в словаре
        dict_local[letter] = round((dict_local.get(letter) / sum(dict_local.values())) * 100, 2)  # Считаем процентное содержание буквы
    return dict_local


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
if __name__ == '__main__':
    dict_letters = get_count_char(main_str)
    print(dict_letters)
    print(ratio_symbol_in_str(dict_letters))
