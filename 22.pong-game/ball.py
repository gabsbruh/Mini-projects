from turtle import Turtle
import constants as c

class Ball(Turtle):
    def __init__(self, color='white'):
        super().__init__()
        self.color(color)
        self.shape('circle')
        self.pu()
        self.setpos(x=0, y=0)
        self.destination = {'x': 580, 'y': 435 }
        
    def move(self):
        self.setpos(self.xcor() + c.BALL_SPEED, self.ycor() + c.BALL_SPEED)