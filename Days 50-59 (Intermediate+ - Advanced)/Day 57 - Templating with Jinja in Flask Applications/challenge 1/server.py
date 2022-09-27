from flask import Flask, render_template
import json
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/guess/<name>')
def guess_who(name):
    response_age = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    response_gender = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    return render_template("otoindex.html",name=name.title(), age=response_age, gender=response_gender)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/97e248619c8bcc50ba7f"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

