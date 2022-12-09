from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for data in question_data:
    new_question = Question(data["question"], data["correct_answer"]) # Creates an object called new_object from the class Question and uses data["text"] and data["answer"] as parameters
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():

    quiz.next_question()

print("You have completed the Quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")