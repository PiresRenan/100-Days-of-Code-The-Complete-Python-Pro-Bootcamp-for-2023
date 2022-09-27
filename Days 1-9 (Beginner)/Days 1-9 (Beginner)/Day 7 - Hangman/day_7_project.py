# HANGMAN 
import random
from Forca_artes import logo, estagios
from Forca_palavras import palavras
print(logo)
print('\n---Bem vindo ao Forca!---\n')

palavra_escolhida = random.choice(palavras).lower()

# 2.0 Pedindo pro usuario inserir uma letra e a verificando dentro da palavra
# 2.1 Criando uma lista vazia e para cada letra da palavra escolhida substituir por '_'
# 2.2 Substituir cada buraco pela letra
# 2.3 Usando os loops, faça o usuario conseguir todas as letras
# 2.4 Iserir a logica para que haja perda de vida por tentativa mal sucedida 
espacos_brancos = []
tamanho_palavra = len(palavra_escolhida)
vidas = 6
for _ in range(tamanho_palavra):
    espacos_brancos += "_"

fim_de_jopo = False
while not fim_de_jopo:
    escolha = input('Digite uma letra: \n').lower()

    for posicao in range(tamanho_palavra):
        letra = palavra_escolhida[posicao]
        if letra == escolha:
            espacos_brancos[posicao] = letra
    
    if escolha not in palavra_escolhida:
        vidas -= 1
        print(estagios[vidas])
        if vidas == 0:
            fim_de_jopo = True
            print('Você perdeu!')


    print(f"{' '.join(espacos_brancos)}")

    if "_" not in espacos_brancos:
        fim_de_jopo = True
        print('Você venceu! ')
