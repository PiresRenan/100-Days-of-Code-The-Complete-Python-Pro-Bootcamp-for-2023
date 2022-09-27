# dicionarios
programa_dicionario = {
    "Bug": "Um erro no programa que o impede de rodar como esperado.", 
    "Função": "Um 'pedaço' do codigo que pode ser chamado diversas vezes facilmente.",
    "Loop": "A ação de repetir."
                        }
#Recuperando itens do dicionario
print(programa_dicionario["Bug"])

#adicionando itens ao dicionario
programa_dicionario["Input"] = "A acão de colher informações do usuario."
print(programa_dicionario,"\n")

#Criar um dicionario vazio
dicionario_vazio = {}

# #Esvaziar o dicionario
# programa_dicionario = {}
# print(programa_dicionario)

#Editar um item no dicionario
programa_dicionario["Bug"] = "Um bicho no computador."
print(programa_dicionario,"\n")

#loop pelo dicionario
for chave in programa_dicionario:
    print(chave)
    print(programa_dicionario[chave])

###################################################################################################
# Aninhado
capitais = {
    "França": "Paris",
    "Alemanha": "Berlim"
            }
#Aninhando uma lista dentro de um dicionario
roteiro_de_viagem = {
    "França": {"cidades_visitadas": ["Paris","Lyon","Dijon"], "numero_visitas": 12},
    "Alemanha":{"cidades_visitadas": ["Berlim","Hamburg","Stutgart"],"numero_visitas": 5}
                     }

#aninhando dicionario em uma lista
roteiro_de_viagem = [
    {
    "país":"França",
    "cidades_visitadas": ["Paris","Lyon","Dijon"], 
    "numero_visitas": 12
    },
    {
    "país":"Alemanho",
    "cidades_visitadas": ["Berlim","Hamburg","Stutgart"], 
    "numero_visitas": 5
    }
]