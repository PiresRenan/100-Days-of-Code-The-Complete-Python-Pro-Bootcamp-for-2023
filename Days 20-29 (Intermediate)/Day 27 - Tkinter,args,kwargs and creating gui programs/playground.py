# Modifique a função add para que pegue um numero ilimitado de numeros como argumentos
# Use a função para somar todos os valores
# Teste isso chamando a função add() para calcular a soma desses argumentos

# def add(*args):
#    print(args[3])
#    total = 0
#    for n in args:
#        total += n
#    return total

# print(add(5, 3, 7, 0, 9, 2, 6))


# Usando a chamada por keywords ao invés do index como no print(args[3])
# cria um dicionario basicamente
# def calculate(**kwargs):
# print(kwargs)
# print(type(kwargs))
# for key, value in kwargs.items():
#    print(key)
#    print(value)
# print(kwargs["add"])

# def calculate(n, **kwargs):
#    print(kwargs)
#    n += kwargs["add"]  # numero 2 add o numero 3 com a keyword "add"
#    n *= kwargs["multiply"]  # multiplicou o numero de tras pelo "multiply" keyword
#    print(n)


# calculate(2, add=3, multiply=5)


# class Car:
#
#     def __init__(self, **kwargs):
#         self.make = kwargs['make']
#         self.model = kwargs['model']
#
#
# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.model)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")  # Usando o .get() o programa não da erro, podendo rodar o codigo tudo sem que
        # o programa crash
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


# Na falta de um dos construtores dá erro, então...
my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
