from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_home():
    return render_template("index.html")


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact")
def get_contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
