# Etch-A-Sketch
from turtle import Turtle, Screen

tata = Turtle()
tela = Screen()


def mover_frente():
    tata.forward(10)


def mover_tras():
    tata.backward(10)


def mover_esquerda():
    new_heading = tata.heading() + 10
    tata.setheading(new_heading)


def mover_direita():
    new_heading = tata.heading() - 10
    tata.setheading(new_heading)


def clear():
    tata.clear()
    tata.penup()
    tata.home()
    tata.pendown()


tela.listen()
tela.onkey(key="w", fun=mover_frente)
tela.onkey(key="s", fun=mover_tras)
tela.onkey(key="a", fun=mover_esquerda)
tela.onkey(key="d", fun=mover_direita)
tela.onkey(clear, "c")
tela.exitonclick()
