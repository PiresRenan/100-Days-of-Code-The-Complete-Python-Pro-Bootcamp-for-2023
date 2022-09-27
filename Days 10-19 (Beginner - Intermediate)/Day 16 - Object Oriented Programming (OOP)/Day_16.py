# Programação Orientada a Objetos Python
## Uso da lib Turtle (https://docs.python.org/3/library/turtle.html)

# import outro_modulo
# print(outro_modulo.outra_variavel)

from random import choice
from turtle import Turtle, Screen

# objeto // classe
timmy = Turtle()
# mostra o espaço na memória alocado para o objeto
print(timmy)
my_screen = Screen().bgcolor("dark grey")
# usando o objeto timmy com alguns metodos da classe turtle
timmy.shape("turtle")
# timmy.color("cyan")
colors = ["cyan", "red", "green", "purple", "white", "black", "yellow"]
for i in range(10):
    for i in range(2):
        timmy.forward(100)
        timmy.right(60)
        timmy.forward(100)
        timmy.right(120)
    timmy.right(36)
    timmy.color(choice(colors))

# my_screen = Screen().bgcolor("blue")
#      Objeto   //  atributo
print(my_screen.canvheight)

#  Objeto // metodo diferencia do atributo pela presença de ()
my_screen.exitonclick()

## Python Pacotes e uso do PyPi (https://pypi.org/)
# from prettytable import PrettyTable
#
# mesa_bonita = PrettyTable()
# mesa_bonita.add_column("Nome Pokemon",
#                        ["Pikachu", "Squirtle", "Charmander"])
# mesa_bonita.add_column("Tipo", ["Elétrico", "Água", "Fogo"])
# mesa_bonita.align = "c"
# print(mesa_bonita)
