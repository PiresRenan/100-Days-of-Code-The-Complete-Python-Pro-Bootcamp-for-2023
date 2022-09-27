# Usando Pandas e lendo arquivos csv

# with open("Dados_previsao_do_tempo.csv") as data_file:
#     data = data_file.readlines()


# Usando a lib do csv nativa do Python para ler arquivos csv
# import csv
#
# with open("Dados_previsao_do_tempo.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)


# Usando a lib Pandas (Que delicinha!!!!!)
import pandas

## com um comando já gera uma tabela formatada ##
data = pandas.read_csv("Dados_previsao_do_tempo.csv")

## seleciona uma coluna pelo nome ##
# print(data["temp"])

## Tabela completamente formatada ##
# print(data)

## Gera um tipo de arquivo "DataFrame" para a tabela completa
# print(type(data))
## Gera um outro para a coluna "Series"
# print(type(data["temp"]))

## Criando dicionarios a partir das colunas
# data_dict = data.to_dict()
# print(data_dict)

## Criando uma lista com os dados da coluna
# temp_list = data["temp"].tolist()
# print(temp_list)
# print(len(temp_list))

## Calculo de media de temp dos 7 dias da semana usando Pandas
# Jeito Python >
# media = sum(temp_list) / len(temp_list)
# print(f"A média das temperaturas dessa semana é de : {round(media)}ºC.")
# Jeito Pandas >
# print(f"A média das temperaturas dessa semana é de : {round(data['temp'].mean())}ºC.")

## Pegando o maior valor de uma tabela
# print(f"A maior temperatura é: {data['temp'].max()}")


## Pegando dados das colunas, usando o nome EXATO da coluna
# print(data['condition'])
# print(data.condition)

## Pegando uma linha de uma tabela
# print(data[data.day == 'Tuesday'])

## Descobrindo qual a maior temperatura e printando todos os seus atributos do dia
# print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
# print(monday.condition)

# # Convertendo a temperatura de segunda para Fahrenheit
# Fahrenheit_temp = (monday.temp * 9/5) + 32
# print(Fahrenheit_temp)
# ## Ou assim >
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

## Criando um DataFrame a partir de um arquivo Python
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data),
# Criando um arquivo CSV a partir dessa lista
# data.to_csv("new_data.csv")
