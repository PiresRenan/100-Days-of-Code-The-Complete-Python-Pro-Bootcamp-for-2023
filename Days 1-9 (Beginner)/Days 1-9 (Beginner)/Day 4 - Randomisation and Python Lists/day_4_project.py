#Pedra, Papel, Tesoura
import random
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print('Bem vindo ao Pedra, Papel e Tesouras\n')

# escolha_jogador = int(input('O que você escolhe? Digite 0 para Pedra, 1 para Papel e 2 para Tesoura'))

# if escolha_jogador == 0:
#     print(pedra)
# elif escolha_jogador == 1:
#     print(papel)
# elif escolha_jogador == 2:
#     print(tesoura)

# print('\n Computador: \n')
# aleatorio = random.randint(0,2)
# if aleatorio == 0:
#     print(pedra)
# elif aleatorio == 1:
#     print(papel)
# elif aleatorio == 2:
#     print(tesoura)

# if aleatorio != escolha_jogador:
#     if aleatorio == 0:
#         if escolha_jogador == 1:
#             print('Parabéns! Você venceu!')
#         elif escolha_jogador == 2:
#             print('Que pena! Você perdeu!')
#     elif aleatorio == 1:
#         if escolha_jogador == 0:
#             print('Parabéns! Você venceu!')
#         elif escolha_jogador == 2:
#             print('Que pena! Você perdeu!')
#     elif aleatorio == 2:
#         if escolha_jogador == 0:
#             print('Parabéns! Você venceu!')
#         elif escolha_jogador == 1:
#             print('Que pena! Você perdeu!')
# else:
#     print('Empate')

##########################################################################################

game_images = [pedra, papel, tesoura]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
