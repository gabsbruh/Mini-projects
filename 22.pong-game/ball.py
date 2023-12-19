from turtle import Turtle
import constants as c
from random import random, randint

class Ball(Turtle):
    def __init__(self, color='white'):
        super().__init__()
        self.color(color)
        self.shape('circle')
        self.pu()
        self.x_move = c.BALL_SPEED
        self.y_move = 0
        self.reset()
        
    def move(self):
        self.setpos(x=self.xcor() + self.x_move, y=self.ycor() + self.y_move)
            
    def reset(self):
        self.setpos(x=0, y=0)
        
    def bounce_wall(self):
        self.y_move *= -1
        
    def bounce_paddle(self):
        self.x_move *= -1
    
    def reset(self):
        self.setpos(x=0, y=0)
        direction = -1 if randint(1,2) == 1 else 1
        self.y_move = random() * c.BALL_SPEED * direction
    
    @property
    def coordinates(self):
        return (self.xcor(), self.ycor())
    
        