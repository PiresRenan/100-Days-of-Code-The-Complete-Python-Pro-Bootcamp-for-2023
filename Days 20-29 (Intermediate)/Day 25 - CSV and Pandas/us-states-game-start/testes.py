import pandas
df = pandas.read_csv("50_states.csv")
states = df["state"].tolist()
resposta_certa = 0
game_is_on = True

while game_is_on:
    print(f"{resposta_certa}/50")
    resposta = input("Digite o nome do Estado:")
    for state in states:
        if resposta == state:
            resposta_certa += 1
