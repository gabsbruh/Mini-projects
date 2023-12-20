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
        self.move_speed = 0.025
        
    def move(self):
        self.setpos(x=self.xcor() + self.x_move, y=self.ycor() + self.y_move)
            
    def reset(self):
        self.setpos(x=0, y=0)
        
    def bounce_wall(self):
        self.y_move *= -1
        
    def bounce_paddle(self):
        self.x_move *= -1 
        self.x_move += self.__randomize()*random()
        self.y_move += self.__randomize()*random()
        self.move_speed *= 0.85
    
    def reset(self):
        self.setpos(x=0, y=0)
        self.y_move = random() * c.BALL_SPEED * self.__randomize() + 0.5
        self
        self.move_speed = 0.025
    
    def __randomize(self):
        return -1 if randint(1,2) == 1 else 1
    
    @property
    def coordinates(self):
        return (self.xcor(), self.ycor())
    
        