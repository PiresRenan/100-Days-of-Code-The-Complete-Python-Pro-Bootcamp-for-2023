# import arts
# import random 

# print(arts.logo1)
# print("\nBem vindo ao jogo de adivinhar!")
# print("Estou pensando em um numero entre 1 e 100.")
# dificuldade = input("Escolha a dificuldade. Escreva 'Facil' ou 'Dificil': ").lower()
# numero_gerado = random.randint(0,100)

# if dificuldade == 'dificil':
#     print(arts.logo3)
#     tentativas = 5
#     for tentativa in range(tentativas):
#         print(f"\nVocê tem {tentativas-tentativa} tentativas para adivinhar o numero.")
#         jogador_chute = int(input("Faça um chute: "))
#         if jogador_chute == numero_gerado:
#             print(f"Parabéns, você acertou!\nA resposta é {numero_gerado}.")
#             break
#         elif jogador_chute > numero_gerado:
#             print("Muito alto!")
#         elif jogador_chute < numero_gerado:
#             print("Muito baixo!")

# if dificuldade == 'facil':
#     print(arts.logo2)
#     tentativas = 10
#     for tentativa in range(tentativas):
#         print(f"\nVocê tem {tentativas-tentativa} tentativas para adivinhar o numero.")
#         jogador_chute = int(input("Faça um chute: "))
#         if jogador_chute == numero_gerado:
#             print(f"Parabéns, você acertou!\nA resposta é {numero_gerado}")
#             break
#         elif jogador_chute > numero_gerado:
#             print("Muito alto!")
#         elif jogador_chute < numero_gerado:
#             print("Muito baixo!")
        
################################# VERSÃO ANGELICA ############################################
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """
    It takes two arguments, a guess and an answer, and prints a message based on whether the guess is
    too high, too low, or correct
    :param guess: The number the user guessed
    :param answer: The correct answer to the question
    """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    """
    It asks the user to choose a difficulty level, and then returns the number of turns that the user
    will have based on their choice
    :return: The number of turns the user has to guess the word.
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # Printing the welcome message, the range of numbers, and the answer.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    print(f"Pssst, the correct answer is {answer}.")

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You've {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return 
        elif guess != answer:
            print("Guess again.")

game()