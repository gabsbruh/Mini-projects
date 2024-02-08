from turtle import Turtle
import turtle

FONT = ("Arial", 8, "bold")
WIN_FONT = ("Arial", 40, "bold")
ALIGNMENT = "center"

class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.color("black")
        self.shape('circle')
        self.speed(0)
    
    def write_state(self, state_name: str, x: float, y: float):
        """Points state and sign it

        Args:
            x (float): x coordination to write
            y (float): y cord to write
        """
        self.pu()
        self.goto(x, y)
        self.write(state_name, align=ALIGNMENT, font=FONT)

    def win(self):
        self.goto(0,0)
        self.write("YOU WIN!", align=ALIGNMENT, font=WIN_FONT)