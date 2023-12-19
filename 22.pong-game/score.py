from turtle import Turtle
from ball import Ball

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.color('white')
        self.score = {'left': 0, 'right': 0}
    
    def left_score_up(self):
        self.score['left'] += 1
    
    def right_score_up(self):
        self.score['right'] += 1