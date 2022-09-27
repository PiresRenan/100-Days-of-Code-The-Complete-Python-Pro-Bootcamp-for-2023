from random import randint

from flask import Flask

app = Flask(__name__)
n_generated = randint(0, 9)


@app.route('/')
def start():
    return "<h1 style='text-align=center'>Guess a number between 0 and 9</h1><br>" \
           "<input type='text' id='fname' name='fname'>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > n_generated:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < n_generated:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
