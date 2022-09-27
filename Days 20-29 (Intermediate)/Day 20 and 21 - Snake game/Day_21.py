# Heranças(Inheritance)

# Declaramos a classe 'filho' e em seguida como argumentos a Classe 'pai'
# class Fish(Animal):
#     def __init__(self):
#  Usasse a palavra-chave 'super' para se referir a classe pai, usando atributos e metodos dela
#         super().__init__()

# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print('Inhale, exhale.')
#
#
# class Fish(Animal):
#
#     def __init__(self):
#         super().__init__()
#
#     def breathe(self):
#         super().breathe()
#         print("doing this underwater.")
#
#     def swim(self):
#         print("moving in water.")
#
#
# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)

### Partindo listas e tuples
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuples = ["do", "re", "mi", "fa", "so", "la", "ti"]
# print(piano_keys[2:5])# da posicao 2 ate a 5
# print(piano_keys[2:])# da posicao 2 ate o fim
# print(piano_keys[:5])# tudo ate o 5
# print(piano_keys[2:5:2])# do 2 e de 2 em 2 ate o 5
# print(piano_keys[::2])# tudo de dois em dois
# print(piano_keys[::-1]) # reverte a lista

print(piano_tuples[2:5])
