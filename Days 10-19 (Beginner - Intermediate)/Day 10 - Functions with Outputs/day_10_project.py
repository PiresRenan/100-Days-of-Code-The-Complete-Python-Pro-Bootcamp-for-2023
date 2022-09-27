from arts import logo

# def soma(primeiro_numero, segundo_numero):
#     total = primeiro_numero + segundo_numero
#     return total

# def subtracao(primeiro_numero, segundo_numero):
#     total = primeiro_numero - segundo_numero
#     return total

# def multiplicacao(primeiro_numero, segundo_numero):
#     total = primeiro_numero * segundo_numero
#     return total

# def divisao(primeiro_numero, segundo_numero):
#     total = primeiro_numero + segundo_numero
#     return total

# repetidor = False
# total = 0

# while not repetidor:
#     print(logo)
#     primeiro_numero = float(input("Qual o primeiro numero?:"))
#     operador = input("Escolha uma operação:")
#     segundo_numero = float(input("Qual o segundo numero?:"))
#     if operador == '+':
#         soma(primeiro_numero,segundo_numero)
#     elif operador == '-':
#         subtracao(primeiro_numero,segundo_numero)
#     elif operador == '*':
#         multiplicacao(primeiro_numero,segundo_numero)
#     elif operador == '/':
#         divisao(primeiro_numero,segundo_numero)
#     else:
#         print("Algum erro encontrado, tente novamente")

#     print(f'{primeiro_numero} {operador} {segundo_numero} = {total}')
#     repetidor = input("Deseja continuar com o numero dado?:")
#     if repetidor == 'n':
#         repetidor = True

###########################################################################################################
def add(n1,n2):
    """
    It takes two numbers as input, adds them together, and returns the result
    :param n1: The first number to add
    :param n2: The second number to add
    :return: The sum of n1 and n2
    """
    return n1 + n2
def sub(n1,n2):
    """
    This function takes two numbers as input and returns the difference between them
    :param n1: The first number
    :param n2: The second number to subtract from the first
    :return: The difference between n1 and n2
    """
    return n1 - n2
def mul(n1,n2):
    """
    It takes two numbers as input and returns their product
    :param n1: The first number
    :param n2: The second number to multiply
    :return: The product of n1 and n2
    """
    return n1 * n2
def div(n1,n2):
    """
    It takes two numbers as input and returns the result of dividing the first number by the second
    number
    :param n1: The first number
    :param n2: The second number to divide
    :return: The result of the division of n1 and n2
    """
    return n1 / n2

# Creating a dictionary with the keys being the operators and the values being the functions.
operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}
def calculator():
    """
    It asks the user for a number, then asks them to pick an operation from a list of operations, then
    asks them for another number, then performs the operation on the two numbers, then asks the user if
    they want to continue calculating with the result of the operation, or start a new calculation
    """
    print(logo)

    n1 = float(input("What's the first number?: "))

    should_continue = True

    while should_continue:
        for operation in operations:
            print(operation)
        operation_symbol = input("Pick an operation from the line above: ")
        n2 = float(input("What's the next number?: "))
        calculation_functions = operations[operation_symbol]
        total = calculation_functions(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {total}")

        if input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ") == 'y':
            n1 = total
        else:
            should_continue = False 
            calculator()
calculator()
