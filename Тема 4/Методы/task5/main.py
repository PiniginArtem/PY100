# TODO реализовать функцию
def get_sentences_list(str_):
    a = []
    for i in str_.split(sep="."):
        if i:
            a.append(i.strip())

    return a


print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
