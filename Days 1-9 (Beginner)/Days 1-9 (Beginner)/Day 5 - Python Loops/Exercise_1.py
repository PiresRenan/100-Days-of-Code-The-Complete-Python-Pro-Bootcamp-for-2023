print('Bem vindo a calculadora de media de altura!\n')
altura_estudantes = input("Digite uma lista de altura dos alunos ").split()
media = 0
cont = 0
for n in range(0, len(altura_estudantes)):
  altura_estudantes[n] = int(altura_estudantes[n])
#   media += altura_estudantes[n]
#   cont += 1
# media = media / cont
# print(round(media))
altura_total = 0
for altura in altura_estudantes:
    altura_total += altura
# print(altura_total)

quantidade_de_alunos = 0
for estudante in altura_estudantes:
    quantidade_de_alunos += 1
# print(quantidade_de_alunos)

media_alturas = round(altura_total / quantidade_de_alunos)
print(media_alturas)
# Instructions 156 178 165 171 187
# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# e.g.
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights
# 1146 ÷ 7 = 163.71428571428572
# Average height rounded to the nearest whole number = 164
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality 
# using what you have learnt about for loops.