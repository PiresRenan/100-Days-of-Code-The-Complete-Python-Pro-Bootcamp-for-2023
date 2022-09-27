from arts import logo
print(logo,"\n")
print("================================================================", '\n')

lances = {}
lances_encerrados = False

def procurar_maior_aposta(apostas_registro):
    maior_aposta = 0
    for apostador in apostas_registro:
        aposta_valor = apostas_registro[apostador]
        if aposta_valor > maior_aposta:
            maior_aposta = aposta_valor
            vencedor = apostador
    print(f"O vencedor é {vencedor} com a aposta de ${maior_aposta}")

while not lances_encerrados:
    name = input('Qual seu nome?: ')
    valor = float(input('Qual teu lance?: $'))
    lances[name] = valor
    continuar = input('Deseja continuar apostando? "Sim" ou "Nao"\n').lower()
    if continuar == 'nao':
        lances_encerrados = True
        procurar_maior_aposta(lances)
    