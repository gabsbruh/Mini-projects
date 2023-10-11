from turtle import Turtle
STARTING_POSITION = (0, 0)
MOVE_DISTANCE = 20
SNAKE_INITIAL_LENGTH = 3

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(SNAKE_INITIAL_LENGTH):
            self.create_segment(STARTING_POSITION[0] + (-20*i), STARTING_POSITION[1])
    
    def create_segment(self, xcord, ycord):
        segment = Turtle(shape="square")
        segment.pu()
        segment.color("white")    
        segment.setpos(xcord, ycord)
        self.segments.append(segment)
        
    def move(self):
        for seg in range(len(self.segments)-1,0,-1): # start,stop, step
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].setpos(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        self.segments[0].left(90)
