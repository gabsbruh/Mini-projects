import random as rnd
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 1
PROBABILITY_OF_NEW_CAR = 0.13

class CarManager(Turtle):
    def __init__(self):
        self.car_list = []
        self.speed = STARTING_MOVE_DISTANCE
        self.probability = PROBABILITY_OF_NEW_CAR
    
    def new(self):
        car = Car()
        self.car_list.append(car)
        
    def possible_new(self): 
        """function that defines a possibility of new() function call
        """      
        return True if rnd.random() <= self.probability else False
        
    def move(self):
        for car in self.car_list:
            car.forward(self.speed)
            if car.xcor() < -320:
                del car

    def next_level(self):
        self.speed += MOVE_INCREMENT
        self.probability += 0.03

    
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid = 0.75, stretch_len=2.2)
        self.pu()
        color = rnd.choice(COLORS)
        self.color(color)
        self.goto(320, rnd.randrange(-255, 265, 20))
        self.setheading(180)