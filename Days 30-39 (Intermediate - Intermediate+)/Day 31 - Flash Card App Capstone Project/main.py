import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_canvas)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_canvas)


def is_known():
    data.remove(current_card)
    new_data = pandas.DataFrame(data)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=626, highlightthickness=0)
card_front_canvas = PhotoImage(file="./images/card_front.png")
card_back_canvas = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_canvas)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

x_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=x_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

v_image = PhotoImage(file="./images/right.png")
right_button = Button(image=v_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
