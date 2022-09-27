import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+',';',',','=']

print('Bem vindo ao gerador de Senhas Python!')
quantidade_letras = int(input('Quantas letras você gostaria de ter na sua senha?\n'))
quantidade_simbolos = int(input('Quantos simbolos você gostaria de ter na sua senha?\n'))
quantidade_numeros = int(input('Quantos numeros você gostaria de ter na sua senha?\n'))
senha = []
for n in range(0, quantidade_letras):
    senha.append(random.choice(letras))
for n in range(0,quantidade_simbolos):
    senha += random.choice(simbolos)
for n in range(0,quantidade_numeros):
   senha += random.choice(numeros)
random.shuffle(senha)
senha_final = ''
for n in senha:
    senha_final += n
print(f'Sua senha sugerida é {senha_final}')

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)
