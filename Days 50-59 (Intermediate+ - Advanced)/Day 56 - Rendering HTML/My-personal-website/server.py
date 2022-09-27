from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def teste_home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)