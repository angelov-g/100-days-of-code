from flask import Flask, render_template
import random
import datetime
import requests

GENDERIZE_ENDPOINT = "https://api.genderize.io"
AGIFY_ENDPOINT = "https://api.agify.io"

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.date.today().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name_input>")
def guess(name_input):
    genderize_response = requests.get(GENDERIZE_ENDPOINT, params={"name": name_input})
    gender_guess = genderize_response.json()["gender"]
    agify_response = requests.get(AGIFY_ENDPOINT, params={"name": name_input})
    age_guess = agify_response.json()["age"]
    return render_template("guess.html", name=name_input.title(), gender=gender_guess, age=age_guess)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    print(num)
    return render_template("blog.html", posts=all_posts)



@app.route("/glog")
def get_glog():
    return "glog page"


if __name__ == "__main__":
    app.run(debug=True)
