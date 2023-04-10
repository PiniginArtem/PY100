students_list = [
    {
        "name": "Саша",
        "age": 27,
    },
    {
        "name": "Кирилл",
        "age": 52,
    },
    {
        "name": "Маша",
        "age": 14,
    },
    {
        "name": "Петя",
        "age": 36,
    },
    {
        "name": "Оля",
        "age": 43,
    },
]

list_ages = [student["age"] for student in students_list]
# print(list_ages)
age = sum(list_ages) / len(list_ages)
# print(age)

students_list_age = [student for student in students_list if student["age"] < age]
print(students_list_age)