# import random
# #i = 100 
#j = 20e7
#gerando um aleatorio entre i e j
#a = random.randrange(i,j)
#try:
#    b = random.randrange(j,i)
#except ValueError:
#    print('ValueError on randrange() since start > stop')
#c = random.randint(100,200)
#try:
#    d = random.randint(200,100)
#except ValueError:
#    print('ValueError on randint() since 200 > 100')
#print('i =', i, " and j =", j)
#print('randrange() generated number: ',a)
#print('randint() generated number: ',c)

#import de um modulo dentro da pasta
#import my_module
#aleatoriedade entre 1 e 10, inclusive
#random_integer = random.randint(1,10)
#print(random_integer)
#print(my_module.pi)
# random_float = random.random()
# print(random_float)
# random_float = random_float*999
# print(random_float)
# love_score = random.randint(1,100)
# print(f"Your love score is {love_score}")

# state1 = "São Paulo"
# state2 = "Rio de Janeiro"
# states_of_Brazil = [state1,state2, 'Minas Gerais', 'Paraná','Bahia','Espirito Santo', 'Mato Grosso','Goias']
# print(states_of_Brazil)
# print(states_of_Brazil[1])
# print(states_of_Brazil[4])
# print(states_of_Brazil[-2])
# states_of_Brazil.append('Acre')
# print(states_of_Brazil)
# states_of_Brazil.extend(['Rondonia','Amazonia','Brasilia','Tocantins','Pernambuco'])
# print(states_of_Brazil)

# str_inp = "Hello,from,AskPython"
# op = str_inp.split(',')
# print(op)

# import random
# a = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'zero']
# print(a)
# for i in range(5):
#     print(random.choice(a))

frutas = ['morangos','tangerina','maçãs','uvas','pêras']
vegetais = ['espinafre','brócolis','cenoura','cebola','alho']

comidas = [frutas,vegetais]

print(comidas)
print(comidas[1])
print(comidas[0][3])