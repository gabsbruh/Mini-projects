from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.starting_position()
        self.left(90)
        self.shape('turtle')
        self.color('green')
        self.shapesize(1, 1)
        
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def starting_position(self):
        self.goto(STARTING_POSITION)
    
    def progress(self):
        return round(((self.ycor() + 280) / 560) * 100) # percentage of progress on level for scoreboard
        