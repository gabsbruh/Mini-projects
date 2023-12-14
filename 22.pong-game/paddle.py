from turtle import Turtle
import constants as c

class Paddle(Turtle):
    def __init__(self, color='white', height=c.PADDLE_HEIGHT):
        super().__init__()
        self.curr_cords = {'x': self.xcor(), 'y': self.ycor()}   
        self.color(color)
        self.shape('square')
        self.shapesize(stretch_wid=height/20, stretch_len=1)
        # this function depends on trutle's orientation, 
        # if headed west/east length parameter streches him horizontally
        # square is 20 by 20
        self.pu()

    def position(self, which_paddle):
        """Set the position of paddle

        Args:
            which_paddle (string): choose 'left' or 'right'
        """
        if which_paddle == 'left':
            self.setpos(x=-(c.SCREEN_WIDTH/2 - 50), y=0)
        elif which_paddle == 'right':
            self.setpos(x=(c.SCREEN_WIDTH/2 - 50), y=0)
        else:
            raise ValueError('Invalid given position where paddle should be placed.')

    def up(self):
        self.curr_cords = {'x': self.xcor(), 'y': self.ycor()}       
        self.sety(self.curr_cords['y'] + 20)

    def down(self):
        self.curr_cords = {'x': self.xcor(), 'y': self.ycor()}       
        self.sety(self.curr_cords['y'] - 20)
        
        