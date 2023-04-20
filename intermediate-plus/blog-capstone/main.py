from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

POSTS_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(POSTS_ENDPOINT)
all_posts = response.json()
posts_list = []
for post in all_posts:
    post_object = Post(post["id"], post["title"], post["subtitle"], post["body"])
    posts_list.append(post_object)


@app.route("/")
def home():
    return render_template("index.html", posts=posts_list)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    requested_post = None
    for post_iter in posts_list:
        if post_iter.id == post_id:
            requested_post = post_iter
    return render_template("post.html", requested_post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
