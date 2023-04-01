# TODO реализовать функцию
def remove_whitespace(str_):
    words = []
    for word in str_.split(sep=" "):
        if word:
            words.append(word)
    return " ".join(words)


str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
