from turtle import Turtle

FONT = ("Courier", 15, "normal")
GAME_OVER_FONT = ("Courier", 30, "bold")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')            
        self.pu()
        self.goto(-220, 260)
        self.write_score()
        self.ht()     
           
    def write_score(self):
        self.write(f'Level: {self.level}/30', align=ALIGNMENT, font = FONT)    
        
    def next_level(self):
        self.level += 1
        self.clear()
        self.write_score()

    def game_over(self, progress):
        self.goto(0,0)
        self.write('GAME OVER!', align=ALIGNMENT, font = GAME_OVER_FONT) 
        self.goto(0,-30)  
        self.write(f'Reached level: {self.level}', align=ALIGNMENT, font = FONT)
        self.goto(0,-60)  
        self.write(f'Progress: {progress}%', align=ALIGNMENT, font = FONT)