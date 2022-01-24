class Quizbrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input("Q."+str(self.question_number)+" "+current_question.text+"(True or False)?").title()
        self.check_answer(answer, self.question_list[self.question_number-1].answer)

    def still_has_questions(self):
        length = len(self.question_list)
        if self.question_number == length:
            return False
        else:
            return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
