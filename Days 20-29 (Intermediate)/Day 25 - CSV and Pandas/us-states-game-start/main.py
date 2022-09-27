# import turtle
# import pandas
# ALINHA = "center"
# FONT = ("Courier", 9, "normal")
# # Colocando uma imagem no Turtle
# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
#
# # # Pegando as posições no mapa, rastreando o click
# # def get_mouse_click_coor(x, y):
# #     print(x, y)
# # turtle.onscreenclick(get_mouse_click_coor)
# # Mantém a janela aberta
# # turtle.mainloop()
# df = pandas.read_csv("50_states.csv")
# states = df["state"].tolist()
# city_name = turtle.Turtle()
# city_name.hideturtle()
# city_name.penup()
#
# coord_x = df["x"].tolist()
# coord_y = df["y"].tolist()
#
#
# correct_answer = 0
# lista_resp_certa = []
# game_is_on = True
# while game_is_on:
#     title = f"{correct_answer}/50 States Correct"
#     answer_state = screen.textinput(title=title, prompt="What's another state's name?")
#     cont = 0
#     for state in states:
#         if answer_state == state:
#             correct_answer += 1
#             lista_resp_certa.append(answer_state)
#             city_name.goto(coord_x[cont], coord_y[cont])
#             city_name.write(f"{state}", align="center", font=FONT)
#         cont += 1


##### CORREÇÃO #####
import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's "
                                                                                             "name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(answer_state) ou
        t.write(state_data.state.item())

states_missed = []
