from flask import Flask, render_template, request
from post import Post
import requests

app = Flask(__name__)

POSTS_ENDPOINT = "https://api.npoint.io/07c01eb3e07ce1edc506"
response = requests.get(POSTS_ENDPOINT)
all_posts = response.json()

posts_list = []
for post in all_posts:
    post_object = Post(post["id"], post["title"], post["subtitle"], post["body"], post["date"], post["image_url"])
    posts_list.append(post_object)


@app.route("/")
def get_home():
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact")
def get_contact():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def get_post(post_id):
    requested_post = None
    for post_iter in posts_list:
        if post_iter.id == post_id:
            requested_post = post_iter
    return render_template("post.html", requested_post=requested_post)


@app.route("/form-entry", methods=["POST"])
def receive_data():
    print(request.form["name"])
    print(request.form["email"])
    print(request.form["phone"])
    print(request.form["message"])
    return "<h1>Successfully sent your message</h1>"


if __name__ == "__main__":
    app.run(debug=True)
