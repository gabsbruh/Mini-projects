import html

class QuizzBrain:
    def __init__(self, question_input, question_number=0, score=0):
        self.question_input = question_input
        self.question_number = question_number
        self.score = score
        
    def next_question(self):
        current_q = self.question_input[self.question_number]
        self.question_number += 1
        user_answer = input(f"Question {self.question_number}. {html.unescape(current_q.text)} write true/false: \t\t")
        return user_answer.capitalize()
        
    def still_questions(self):
        return self.question_number < len(self.question_input)
        
    def if_correct(self, user_answer):
        if self.question_input[self.question_number-1].answer == user_answer:
            self.score += 1 
            print(f"You're right! Your current score is {self.score}/{self.question_number}")
        else:
            print(f"You're wrong. Your current score is {self.score}/{self.question_number}")
            
        
