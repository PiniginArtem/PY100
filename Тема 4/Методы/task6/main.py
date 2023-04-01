# TODO реализовать функцию
def get_unique_words(str_):
    words = list(set(str_.split()))
    words.sort()
    return words


print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
