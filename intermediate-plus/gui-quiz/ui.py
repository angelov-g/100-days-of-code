from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TEXT_FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Some text here",
                                                     fill=THEME_COLOR,
                                                     font=TEXT_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        image_true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=image_true, highlightthickness=0, command=self.click_true)
        self.true_button.grid(row=2, column=0)

        image_false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=image_false, highlightthickness=0, command=self.click_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def click_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def click_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
