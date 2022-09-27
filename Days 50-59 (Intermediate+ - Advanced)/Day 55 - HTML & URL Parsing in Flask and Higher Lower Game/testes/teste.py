from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1 style="text-align: center">Oi!</h1><br>' \
           '<div style="width:100%;height:0;padding-bottom:135%;margin-left=30%;position:relative;"><iframe src="https://giphy.com/embed/l2JI3dSEKmK0a3bby" width="20%" height="20%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>'


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Tchau!'


# O "name" é uma variavel
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


# @app.route('/username/<name>')
# def greet(name):
#     return f"Hello {name}"
# @app.route('/<name>')
# def greet(name):
#     return f"Hello {name}"

# if __name__ == "__main__":
#     app.run()
# podemos fazer atualizações sem precisar ficar desligando e ligando o servidor
if __name__ == "__main__":
    app.run(debug=True)
