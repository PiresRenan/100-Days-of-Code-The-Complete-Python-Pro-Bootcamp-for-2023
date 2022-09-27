print('Bem vindo a Roleta da Conta')
import random
gerador = int(input('Digite um numero pra escolher:'))
random.seed(gerador)

nomes_coleta = input('Dê o nome de todos, separados por virgula: ')
names = nomes_coleta.split(',')
choosen = random.choice(names)
print(choosen + " é a pessoa que vai pagar hoje!")
# choosen = names[random.randint(0,len(names)-1)]
# print(f'{choosen} is going to buy the meal today!')
#randomico = random.randint(0,len(nomes)-1)
# print(nomes[randomico])
# Banker Roulette
# Instructions
# You are going to write a program that will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them inside a 
# List called names. For this to work, you must enter all the names as names followed
# by comma then space. e.g. name, name, name
# When you run the code, just use a random number as the seed. e.g. 67346 It doesn't 
# matter what you chose, it's only for our testing code to check your work.