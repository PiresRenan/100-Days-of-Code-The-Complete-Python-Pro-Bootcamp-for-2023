print("Bem vindo a calculadora do amor!")
nome1 = input("Qual o seu nome? \n")
nome2 = input("Qual o nome dela? \n")

nome1 = nome1.lower()
nome2 = nome2.lower()

contador1 = nome1.count('t') + nome2.count('t') + nome1.count('r') + nome2.count('r') + nome1.count('u') + nome2.count('u') + nome1.count('e') + nome2.count('e')
contador2 = nome1.count('l') + nome2.count('l') + nome1.count('o') + nome2.count('o') + nome1.count('v') + nome2.count('v') + nome1.count('e') + nome2.count('e')

total_do_amor = (contador1 * 10) + contador2

if total_do_amor < 10 or total_do_amor > 90:
    print(f'Sua pontuação é de {total_do_amor}, vocês combinam como coca e mentos.')
elif total_do_amor >= 40  and total_do_amor <= 50:
    print(f'Sua pontuação é de {total_do_amor}, vocês estão bem juntos.')
else:
    print(f'Sua pontuação é de {total_do_amor}')
#Love Calculator
#Instructions
#You are going to write a program that tests the compatibility between two people.
#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. 
#Then combine these numbers to make a 2 digit number.
#For Love Scores less than 10 or greater than 90, the message should be:
#"Your score is **x**, you go together like coke and mentos."
#For Love Scores between 40 and 50, the message should be:
#"Your score is **y**, you are alright together."
#Otherwise, the message will just be their score. e.g.:
#"Your score is **z**."
#e.g.
#name1 = "Angela Yu"
#name2 = "Jack Bauer"
#T occurs 0 times
#R occurs 1 time
#U occurs 2 times
#E occurs 2 times
#Total = 5
#L occurs 1 time
#O occurs 0 times
#V occurs 0 times
#E occurs 2 times
#total = 3
#Love Score = 53
#Print: "Your score is 53."