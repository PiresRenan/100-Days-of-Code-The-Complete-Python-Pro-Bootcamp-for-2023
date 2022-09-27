print('Bem vindo ao Mapa do Tesouro')
linha1 = ["⬜️","⬜️","⬜️"]
linha2 = ["⬜️","⬜️","⬜️"]
linha3 = ["⬜️","⬜️","⬜️"]
mapa = [linha1, linha2, linha3]
print(f"{linha1}\n{linha2}\n{linha3}")
posicao = input("\nOnde quer colocar o tesouro? \n")
horizontal = int(posicao[0])-1
vertical = int(posicao[1])-1
mapa[horizontal][vertical] = 'X'
# if posicao[0] == '1':
#     if posicao[1] == '1':
#         linha1[0] = 'X'
#     elif posicao[1] == '2':
#         linha2[0] = 'X'
#     elif posicao[1] == '3':
#         linha3[0] ='X'
#     else:
#         print('Entrada errada')
# elif posicao[0] == '2':
#     if posicao[1] == '1':
#         linha1[1] = 'X'
#     elif posicao[1] == '2':
#         linha2[1] = 'X'
#     elif posicao[1] == '3':
#         linha3[1] ='X'
#     else:
#         print('Entrada errada')
# elif posicao[0] == '3':
#     if posicao[1] == '1':
#         linha1[2] = 'X'
#     elif posicao[1] == '2':
#         linha2[2] = 'X'
#     elif posicao[1] == '3':
#         linha3[2] ='X'
#     else:
#         print('Entrada errada')
# else:
#     print('Entrada errada')
print(f"\n{linha1}\n{linha2}\n{linha3}")

#Treasure Map
# Instructions
# You are going to write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like:
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# In the starting code, we have used new lines (\n) to format the three rows into a square, like this:
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# This is to try and simulate the coordinates on a real map.
# Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
# The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:
# First, your program must take the user input and convert it to a usable format.
# Next, you need to use it to update your nested list with an "x".