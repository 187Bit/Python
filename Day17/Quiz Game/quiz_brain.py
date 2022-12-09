class QuizBrain:

    def __init__(self, question_bank) -> None:
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self): # Always use the self parameter
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Question {self.question_number}: {current_question.text} (True/False)?:\n")
        self.check_answer(user_input, current_question.answer)
    
    def still_has_questions(self):

        return self.question_number < len(self.question_list)

    def check_answer(self, user_input, question_answer):
        
        if user_input.lower() == question_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got in wrong!")
        
        print(f"The correct answer was: {question_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")