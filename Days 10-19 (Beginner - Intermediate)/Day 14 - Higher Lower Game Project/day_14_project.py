from arts import logo, vs
from game_data import data
from random import randint

print(logo)

choosen_one = []
A = {}
B = {}
score = 0
def choose_data(aleatorio):
    return choosen_one.append(data[aleatorio])

def comparar(choosen_one):
    A.update(choosen_one[0].items())
    B.update(choosen_one[1].items())
    if choosen_one[0].items() == choosen_one[1].items():
        choosen_one[0].update(data[aleatorio])
        comparar(choosen_one)
    else:
        if A.get('follower_count') > B.get('follower_count'):
            maior = choosen_one[0]
            choosen_one.clear()
        else:
            maior = choosen_one[1]
            choosen_one.clear()

continua = True
while continua:
    for i in range(2):
        aleatorio = randint(0,49)
        choose_data(aleatorio)
    print(f"Comparação A: {choosen_one[0].get('name')}, a {choosen_one[0].get('description')}, from {choosen_one[0].get('country')}.")
    # print(f"Pontos {choosen_one[0].get('follower_count')}")
    print(vs)
    print(f"Comparação B: {choosen_one[1].get('name')}, a {choosen_one[1].get('description')}, from {choosen_one[1].get('country')}.\n")
    # print(f"Pontos {choosen_one[1].get('follower_count')}")
    comparar(choosen_one)
    resposta = input("Quem tem mais seguidores? Escreva 'A' ou 'B': ").lower()
    if resposta == 'a' and A.get('follower_count') > B.get('follower_count'):
        score += 1
        print(f"\nEstá correto! Sua pontuação atual é {score}.\n")
    elif resposta == 'b' and A.get('follower_count') < B.get('follower_count'):
        score += 1
        print(f"\nEstá correto! Sua pontuação atual é {score}.\n")
    else:
        print(f"\nVocê fez {score} pontos.")
        if input("\nDeseja jogar outra partida? Digite 'S' ou 'N':").lower() == 'n':
            continua = False
        else:
            print('\n')
            score = 0