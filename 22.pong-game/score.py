from turtle import Turtle
from ball import Ball
import constants as c

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.color('white')
        self.score = {'left': 0, 'right': 0}
        self.update()
    
    def left_score_up(self):
        self.score['left'] += 1
    
    def right_score_up(self):
        self.score['right'] += 1
    
    def update(self):
        self.clear()
        align, font = c.WRITING_OPTIONS
        self.goto(c.WRITE_SCORE_LEFT)
        self.write(self.score['left'], align=align, font=font)
        self.goto(c.WRITE_SCORE_RIGHT)
        self.write(self.score['right'], align=align, font=font)
        
    def endgame_statement(self):
        align, font = c.ENDGAME_WRITING_OPTIONS
        self.setpos(0,100)
        if self.score['left'] == c.FINAL_SCORE:
            self.write("Left side player is victorious!", align=align, font=font)
        if self.score['right'] == c.FINAL_SCORE:
            self.write("Right side player is victorious!", align=align, font=font)
        