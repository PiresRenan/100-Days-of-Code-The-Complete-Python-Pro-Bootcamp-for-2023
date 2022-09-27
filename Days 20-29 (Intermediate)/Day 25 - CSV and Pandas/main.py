# Esquilos no Central Park NY

import pandas
dados = pandas.read_csv("Censo_Esquilos_2018_CentralPark.csv")
# print(dados['Primary Fur Color'])
cor_esquilo = dados['Primary Fur Color'].tolist()
esquilo_marrom = 0
esquilo_preto = 0
esquilo_cinza = 0
esquilo_NaN = 0

for esquilo in cor_esquilo:
    if esquilo == 'Cinnamon':
        esquilo_marrom += 1
    elif esquilo == 'Gray':
        esquilo_cinza += 1
    elif esquilo == 'Black':
        esquilo_preto += 1
    else:
        esquilo_NaN += 1


print(f"No ano de 2018, no Central Park (Nova Iorque), existiam:\n{esquilo_preto} esquilos pretos,"
      f"\n{esquilo_cinza} esquilos cinza e\n{esquilo_marrom} esquilos marrom.\nE {esquilo_NaN} "
      f"esquilos sem cor definida.")


## Correção ##
import pandas
# Criando um DataFrame dos dados
data = pandas.read_csv("Censo_Esquilos_2018_CentralPark.csv")
#Criando um Series
# grey_squirel = data[data["Primary Fur Color"] == "Gray"]
# print(grey_squirel)
grey_squirel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirel_count = len(data[data["Primary Fur Color"] == "Black"])
print()
print(black_squirel_count)
print(grey_squirel_count)
print(red_squirel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirel_count, red_squirel_count, black_squirel_count]
}

df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")

