import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f'00:00')
    label_title.config(text="Timer")
    label_check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_title.config(text="BREAK", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        label_title.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        label_title.config(text="Work", fg=GREEN)
        countdown(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if len(str(count_min)) < 2:
        count_min = f'0{count_min}'
    if len(str(count_sec)) < 2:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += CHECK_MARK
        label_check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="START", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="RESET", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

label_title = Label(text="Timer", fg=GREEN, bg=YELLOW)
label_title.config(font=(FONT_NAME, 50))
label_title.grid(column=1, row=0)

label_check = Label()
label_check.config(font=("Arial", 20), fg=GREEN, bg=YELLOW)
label_check.grid(column=1, row=3)

window.mainloop()
