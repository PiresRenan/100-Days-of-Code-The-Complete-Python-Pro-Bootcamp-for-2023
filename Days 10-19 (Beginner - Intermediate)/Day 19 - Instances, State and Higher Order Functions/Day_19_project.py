# from turtle import Turtle, Screen
# from random import randint
#
# p1 = Turtle()
# vs = Turtle()
# criador = Turtle()
# criador.hideturtle()
# p1.hideturtle()
# vs.hideturtle()
# screen = Screen()
#
# criador.penup()
# criador.goto(300, -25)
# criador.pendown()
# criador.pensize(5)
# criador.goto(300, 75)
# p1.shape("turtle")
# p1.color("Red")
# p1.penup()
# p1.goto(-325, 0)
# p1.showturtle()
# vs.shape("turtle")
# vs.color("Blue")
# vs.penup()
# vs.goto(-325, 50)
# p1.showturtle()
# vs.showturtle()
#
#
# def move_forward():
#     p1.forward(10)
#     vs.forward(randint(0, 20))
#
#
# screen.listen()
# screen.onkey(move_forward, "space")
#
# screen.exitonclick()

from random import randint
## CORREÇÃO ##
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Faça sua aposta", prompt="Qual a tartaruga vencedora? Escolha uma cor:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
