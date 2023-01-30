from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
current_card = {}
to_learn = {}

# -------------------- WORD DATA ------------------- #
try:
    word_df = pandas.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_word_df = pandas.read_csv("data/french_words.csv")
    word_dict = original_word_df.to_dict(orient="records")
else:
    word_dict = word_df.to_dict(orient="records")


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)

    current_card = choice(word_dict)
    french_translation = current_card["French"]

    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_translation, fill="black")

    flip_timer = window.after(3000, flip_card)


def flip_card():
    english_translation = current_card["English"]

    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_translation, fill="white")


def knows_word():
    word_dict.remove(current_card)
    data = pandas.DataFrame(word_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# -------------------- UI SETUP -------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, command=knows_word)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
