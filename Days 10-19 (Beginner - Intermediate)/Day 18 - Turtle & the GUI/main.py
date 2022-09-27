###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
# from turtle import *
# from random import *

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#    rgb_colors.append(color.rgb)

# tata = Turtle()
# turtle.colormode(255)
# tata.shape("circle")
# tata.speed("fastest")
# tata.shapesize(0.5)
# tata.pensize(15)

# def random_cor():
#    cor_escolhida = choice(rgb_colors)
#    cor = (cor_escolhida.r, cor_escolhida.g, cor_escolhida.b)
#    tata.color(cor)


# def criando_obra_prima():
#    random_cor()
#    tata.forward(0)
#    tata.penup()
#    tata.forward(20)
#    tata.pendown()


# def reposicionar():
#    tata.penup()
#    tata.left(90)
#    tata.forward(20)
#    tata.left(90)
#    tata.forward(660)
#    tata.pendown()
#    tata.left(180)


# def inicio():
#    tata.penup()
#    tata.right(90)
#    tata.forward(265)
#    tata.right(90)
#    tata.forward(325)
#    tata.pendown()
#    tata.right(180)


# inicio()
# for _ in range(28):
#    for i in range(33):
#        criando_obra_prima()
#    reposicionar()

# screen = Screen()
# screen.exitonclick()

## CORREÇÃO ##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

# print(rgb_colors )

import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()

tim.hideturtle()

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
