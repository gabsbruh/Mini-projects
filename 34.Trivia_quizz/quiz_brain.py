import html

class QuizzBrain:
    def __init__(self, question_input, question_number=0, score=0):
        self.question_input = question_input
        self.question_number = question_number
        self.score = score
        
    def next_question(self):
        current_q = self.question_input[self.question_number]
        self.question_number += 1
        user_answer = f"Question {self.question_number}. {html.unescape(current_q.text)} write true/false: \t\t"
        return user_answer.capitalize()
        
    def still_questions(self):
        return self.question_number < len(self.question_input)
        
    def check_answer(self, user_answer: str):
        if self.question_input[self.question_number].answer.lower() == user_answer.lower():
            return True
        else:
            return False
