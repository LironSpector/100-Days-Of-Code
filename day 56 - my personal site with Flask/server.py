from flask import Flask, render_template

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/')
def hello_world():
    return render_template("Liron.html")


# @app.route("/<int:guess>")
# def guess_number(guess):
#     if guess > random_num:
#         print("A", random_num)
#         return "<h1 style='color: purple'>Too high, try again!</h1>" \
#                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
#     elif guess < random_num:
#         print("B", random_num)
#         return "<h1 style='color: red'>Too low, try again!</h1>"\
#                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
#     else:
#         return "<h1 style='color: green'>You found me!</h1>" \
#                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
