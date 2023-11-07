from turtle import Turtle
import random as rnd

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.new_food_pos()
    
    def new_food_pos(self):
        rnd_x = rnd.randint(-280, 280)
        rnd_y = rnd.randint(-280, 280)
        self.goto(rnd_x, rnd_y)
        return rnd_x, rnd_y