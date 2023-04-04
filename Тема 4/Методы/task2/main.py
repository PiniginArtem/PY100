def is_palindrome(str_):
    a = str_.lower().replace(" ", "")  # TODO привести строку к единому регистру и избавиться от пробелов
    if a == a[::-1]:  # TODO проверка палиндрома
        print("Строка палиндром")
    else:
        print("Строка не палиндром")


is_palindrome("Кит на море не романтик")
is_palindrome("Прочая строка")
