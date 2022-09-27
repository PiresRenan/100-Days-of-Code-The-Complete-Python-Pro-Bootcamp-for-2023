### Debugging

# #Descreva o problema
# def add():
#     for i in range(1,20):
#         if i == 20:
#             print("You got it")
# add()
# #não printa pois o range é menor que o if

# #Reproduzir o bug
# from random import randint
# dice_imgs = ["1","2","3","4","5","6"]
# dice_num = randint(1,6)
# print(dice_imgs[dice_num])
# #os index dentro da lista são menores que o randint, ocasionando o bug. Deve-se diminuir para 0/5, acompanhando a indexação do dice_imgs.

# #Play Computer
# year = int(input("Qual seu ano de nascimento?"))
# if year > 1980 and year < 1994:
#     print("You're a millenial.")
# elif year > 1994:
#     print("You're a Gen Z.")
# #os ifs nao estão incluindo o ano de 1994

# #Consertando Errors
# age = input("Quantos anos você tem?")
# if age > 18:
# print("Você pode dirigir com age {age}.")
# #Erros estão na posição do print, desrespeitando a formatação do Python3, além de estar sem a justificativa "print(f'...')"

# #Print é sua amiga
# pages = 0
# word_per_page = 0
# pages = int(input("Numero de pagina: "))
# word_per_page == int(input("Numero de palavras por pagina: "))
# total_words = pages * word_per_page
# print(total_words)
# #Colocando dois prints para vermos onde estão os erros, encontramos o erro na sinalização da variavel word_per_page, onde está usando um operador comparativo, ao invés de um determinador.

#Use o Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)
mutate([1,2,3,5,8,13])
#Usando o debugger podemos notar que apenas o ultimo valor está sendo incluido na lista, podemos consertar este bug colocando o .append(new_item) para dentro do for.

