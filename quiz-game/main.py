from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for new_question in question_data:
    question_object = Question(new_question["text"], new_question["answer"])
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()