from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []

for i in range(0, len(question_data)):
    question_text = Question(question_data[i]['question'], question_data[i]['correct_answer'])
    question_bank.append(question_text)

brain = Quizbrain(question_bank)

while brain.still_has_questions():
    brain.next_question()

print("Congratulations! You've completed the quiz!")
print(f"Your final score was: {brain.score}/{brain.question_number}")
