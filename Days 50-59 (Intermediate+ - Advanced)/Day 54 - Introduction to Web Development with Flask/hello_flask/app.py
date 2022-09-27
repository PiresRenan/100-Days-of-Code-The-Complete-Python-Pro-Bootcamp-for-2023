from flask import Flask
app = Flask(__name__)

# http://127.0.0.1:5000/ home page
@app.route('/')
def hello_world():
    return 'OI MUNDO'

# http://127.0.0.1:5000/bye another page
@app.route('/bye')
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()