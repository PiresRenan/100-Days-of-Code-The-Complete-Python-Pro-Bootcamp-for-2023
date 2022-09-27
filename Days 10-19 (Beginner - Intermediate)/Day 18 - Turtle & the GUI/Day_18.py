# from turtle import Turtle, Screen
# from random import choice

# new_turtle = Turtle()
# tom = Turtle()
# terry = Turtle()

# new_turtle.shape("turtle")  #“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.
# tom.shape("circle")
# terry.shape("classic")

# new_turtle.color("Red")
# tom.color("Blue")
# terry.color("Green")

# colors = ["Black", "Navy", "DodgerBlue", "DeepSkyBlue", "Cyan", "MintCream", "MediumSeaGreen", "PaleGreen", "Chartreuse", "Goldenrod", "Red", "MistyRose",
#          "DeepPink", "Purple", "BlueViolet", "MediumSlateBlue", "Indigo"]


# def square():
#    for i in range(4):
#        new_turtle.forward(250)
#        new_turtle.right(90)

# square()

# screen = Screen()
# screen.exitonclick()


# Em Python podemos renomear um modulo para facilitar a compreensao
# import turtle as t
# new_turtle = t.Turtle()

# Podemos achar milhares de modulos interessantes usando o PyPI
# import heroes
# print(heroes.gen())

# from turtle import Turtle, Screen
# from random import choice

# colors = ["red", "blue", "green", "violet", "grey", "black", "grey"]
# tata = Turtle()


# def quadrado_tracejado():
#    tata.color(choice(colors))
#    for i in range(4):
#        for i in range(20):
#            if i % 2 == 0:
#                tata.forward(5)
#                tata.penup()
#            else:
#                tata.forward(5)
#                tata.pendown()
#        tata.right(90)

# def formas():
#    num_sides = 2
#    for _ in range(7):
#        num_sides += 1
#        angulo = 360 / num_sides
#        tata.color(choice(colors))
#        for i in range(num_sides):
#            tata.forward(100)
#            tata.right(angulo)


# formas()

# screen = Screen()
# screen.exitonclick()


# Random walk
# from turtle import *
# from random import choice, randint

# colors = ["red", "blue", "green", "violet", "grey", "black", "grey"]
# tata = Turtle()
# turtle.colormode(255)
# tata.shape("circle")
# tata.pensize(2.5)
# tata.shapesize(0.25)
# tata.speed(1000)


# def random_walk(direcao, angulo):
#    if direcao == 1:
#        tata.right(angulo)
#    else:
#        tata.left(angulo)
#    tata.forward(25)


# for i in range(200):
#    r = randint(0, 255)
#    g = randint(0, 255)
#    b = randint(0, 255)
#    tata.color((r, g, b))
#    angle = randint(90, 270)
#    direction = randint(1, 2)
#    random_walk(direction, angle)

# screen = Screen()
# screen.exitonclick()
# import turtle
# from turtle import *
# from random import randint
# screen = Screen()
# screen.exitonclick()
import turtle
from random import randint
from turtle import *

turtle.colormode(255)
tata = Turtle()
tata.speed("fastest")
tata.pensize(2)
tata.shapesize(0.05)


def randomize_colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


def draw_sphirograph(tamanho):
    for i in range(int(360 / tamanho)):
        tata.color(randomize_colors())
        tata.circle(100)
        tata.left(tamanho)


draw_sphirograph(5)

screen = Screen()
screen.exitonclick()
