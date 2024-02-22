from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))

quiz = QuizzBrain(question_bank)

while quiz.still_questions():
    user_answer = quiz.next_question()
    quiz.if_correct(user_answer)
print(f"That's the end of the quiz. Your final score is {quiz.score}/{quiz.question_number}")