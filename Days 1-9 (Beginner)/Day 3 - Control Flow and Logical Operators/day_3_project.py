#treasure island
print("Bem vindo a Ilha do Tesouro.\nSua missão é encontrar o tesouro.")

decisao = input("Esquerda ou direita?").lower()
if decisao == "esquerda":
    decisao = input('Nadar ou Esperar?').lower()
    if decisao == "esperar":
        decisao = input('Qual porta? Azul, vermelha ou amarela?').lower()
        if decisao == "azul":
            print("Comido por animais selvagens.\nFIM DE JOGO.")
        elif decisao == "vermelha":
            print('Queimado vivo.\nFIM DE JOGO.')
        elif decisao == "amarela":
            print('VOCÊ VENCEU!!!')
        else:
            print('FIM DE JOGO.')
    else:
        print('Atacado por uma truta.\nFIM DE JOGO.')
else:
    print('Caiu em um buraco.\nFIM DE JOGO.')