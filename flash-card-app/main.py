from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# -------------------- WORD DATA ------------------- #
word_df = pandas.read_csv("data/french_words.csv")
word_dict = word_df.to_dict(orient="records")


def random_word():
    french_word = choice(word_dict)["French"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=french_word)



# -------------------- UI SETUP -------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=random_word)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, command=random_word)
right_button.grid(row=1, column=1)

random_word()

window.mainloop()
