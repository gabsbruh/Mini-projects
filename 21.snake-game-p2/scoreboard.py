from turtle import Turtle
FONT = ('Courier', 15, 'normal')
ALIGNMENT = 'center'
GAME_OVER_FONT = ('Courier', 30, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')            
        self.pu()
        self.goto(0, 270)
        self.write_score()
        self.ht()     
        
    def write_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font = FONT)
    
    def score_up(self):
        self.score += 1
        self.clear()
        self.write_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER!', align=ALIGNMENT, font = GAME_OVER_FONT) 
        self.goto(0,-30)  
        self.write(f'Your Score: {self.score}', align=ALIGNMENT, font = FONT)
    
    def current_score(self):
        return self.score