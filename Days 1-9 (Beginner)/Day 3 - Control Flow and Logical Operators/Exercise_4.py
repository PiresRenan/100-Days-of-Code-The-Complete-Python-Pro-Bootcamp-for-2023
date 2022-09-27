print("Bem vindo a Entrega Python Pizza")
tamanho = input("Qual tamanho de pizza quer? P, M, or G ")
adc_pepperoni = input("Você quer adicionar pepperone? S or N ")
extra_queijo = input("Você quer queijo extra? S or N ")

conta = 0
if tamanho == "P":
    conta = 15
    if adc_pepperoni == "S":
        conta += 2
    if extra_queijo == "S":
        conta += 1
elif tamanho == "M":
    conta = 20
    if adc_pepperoni == "S":
        conta += 3
    if extra_queijo == "S":
        conta += 1
elif tamanho == "G":
    conta = 25
    if adc_pepperoni == "S":
        conta += 3
    if extra_queijo == "S":
        conta += 1
else:
    print("Tamanho invalido")

print(f'O preço total a pagar é de R${conta},00')
#Pizza Order Practice
#Instructions
#Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
#Based on a user's order, work out their final bill.
#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1