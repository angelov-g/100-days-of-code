from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://em-content.zobj.net/thumbs/120/apple/354/smiling-face-with-smiling-eyes_1f60a.png">'


@app.route("/bye")
def bye():
    return "Bye"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)
