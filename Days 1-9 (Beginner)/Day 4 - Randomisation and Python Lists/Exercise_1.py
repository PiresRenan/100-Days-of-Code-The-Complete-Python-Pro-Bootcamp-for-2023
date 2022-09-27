import random
print('Bem vindo ao Cara ou Coroa')
semente_teste = int(input("Digite um numero de semente: "))
random.seed(semente_teste)
cara_ou_coroa = random.randint(0,1)
if cara_ou_coroa != 0:
    print('Coroa')
else:
    print('Cara')
#Heads or Tails
#Instructions
#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
#Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
#When you run the code, just use a random number as the seed. e.g. 67346 It doesn't matter what you chose, it's only for our testing code to check your work.
#There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.
#e.g. 1 means Heads 0 means Tails