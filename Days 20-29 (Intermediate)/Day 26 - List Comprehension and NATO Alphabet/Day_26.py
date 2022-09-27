# Compreensão de lista
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# double_range = [n*2 for n in range(1, 5)]
# print(double_range)

# Condicional compreensão de lista
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# lista = [item_novo for item in lista if teste]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# novos_nomes = [name.upper() for name in names if len(name) > 5]
# print(novos_nomes)

# Compreensão de dicionario
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_scores = {student: random.randint(30, 100) for student in names}
# passed_students = {student: score for (student, score) in students_scores.items() if score > 70}
# print(passed_students)

# Usando pandas loop DataFrame
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# Looping pelos dicionarios:
# for (key, value) in student_dict.items():
#    print(value)

import pandas

student_DataFrame = pandas.DataFrame(student_dict)
# print(student_DataFrame)

# Loop atraves um Data Frame:
# for (key, value) in student_DataFrame.items():
#    print(key)
#    print(value)

# Loop através das linhas do Data Frame
for (index, row) in student_DataFrame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)
