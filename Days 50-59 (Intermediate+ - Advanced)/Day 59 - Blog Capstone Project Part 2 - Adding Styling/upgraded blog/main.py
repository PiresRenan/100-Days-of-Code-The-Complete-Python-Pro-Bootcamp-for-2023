from turtle import pos
from flask import Flask, render_template
import requests

app = Flask(__name__)
posts = requests.get('https://api.npoint.io/2ed8dd2cd26362e7d81f').json()
@app.route('/index.html')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
    