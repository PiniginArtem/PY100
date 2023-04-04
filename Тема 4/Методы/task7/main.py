students_dict = {
    'Саша': 27,
    'Кирилл': 52, 
    'Маша': 14, 
    'Петя': 36, 
    'Оля': 43, 
}
# ages = 0
# for age in students_dict.values():
#     ages += age
# ages /= len(students_dict.values())
# print(ages)

print(sum(students_dict.values()) / len(students_dict))
