print('Bem vindo ao maior pontuação\n')
placar_estudantes = input("Digite a pontuação dos alunos ").split()
for n in range(0, len(placar_estudantes)):
  placar_estudantes[n] = int(placar_estudantes[n])
print(placar_estudantes)

# funcoes max e min
# print(max(placar_estudantes))
# print(min(placar_estudantes))

maior_pontuacao = 0
for n in placar_estudantes:
    if n > maior_pontuacao:
         maior_pontuacao = int(n)

print(f"A maior pontuação da clasee é {maior_pontuacao}")
# High Score  78 65 89 86 55 91 64 89

# Instructions
# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions. The output words must match
# the example. i.e
# The highest score in the class is: x