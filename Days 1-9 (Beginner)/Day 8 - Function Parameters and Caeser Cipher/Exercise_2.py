def primo_ou_nao(numero):
    eh_primo = True
    for i in range(2,numero):
        if numero % i == 0:
            eh_primo = False
    if eh_primo:
        print("É um numero primo.")
    else:
        print("Não é um numero primo.")

numero = int(input('Digite um numero: '))
primo_ou_nao(numero )


# Prime Numbers
#    Instructions
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# https://en.wikipedia.org/wiki/Prime_number
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# Here are the numbers up to 100, prime numbers are highlighted in yellow:

