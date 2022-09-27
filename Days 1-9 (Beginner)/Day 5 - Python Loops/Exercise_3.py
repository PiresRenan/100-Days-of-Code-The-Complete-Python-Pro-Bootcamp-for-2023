print('Bem vindo ao somador de numeros pares')
# numeros = input("Digite os numeros a serem somados ").split()
# total = 0
# for n in range(0,len(numeros)):
#     numeros[n] = int(numeros[n])
#     if numeros[n] % 2 == 0 and numeros[n] != 0:
#         total += numeros[n]

total = 0
for n in range(2,101, 2):
    total += n

print(total)
#Adding Even Numbers
# Instructions
# You are going to write a program that calculates the sum of all the even numbers 
# from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# Important, there should only be 1 print statement in your console output. It should
#just print the final total and not every step of the calculation.