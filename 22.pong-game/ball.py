from turtle import Turtle
import constants as c
from random import randint

class Ball(Turtle):
    def __init__(self, color='white'):
        super().__init__()
        self.color(color)
        self.shape('circle')
        self.pu()
        self.setpos(x=0, y=0)
        # self.destination = {'x': 580, 'y': 435 }
        self.x_move = c.BALL_SPEED
        self.y_move = randint(1,c.BALL_SPEED)
        
    def move(self):
        self.setpos(self.xcor() + self.x_move, self.ycor() + self.y_move)
            
    def bounce_wall(self):
        self.y_move *= -1
        
    def bounce_paddle(self):
        self.x_move *= -1
        