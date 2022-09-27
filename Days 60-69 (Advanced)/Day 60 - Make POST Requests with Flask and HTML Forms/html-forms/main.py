from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']
        return f'<h1>Nome = {nome}<br>Senha = {senha}'


if __name__ == '__main__':
    app.run(debug=True)
