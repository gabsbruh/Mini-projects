from turtle import Turtle
FONT = ('Courier', 15, 'normal')
ALIGNMENT = 'center'
GAME_OVER_FONT = ('Courier', 30, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('score.txt', 'r') as high_score:
            self.high_score = int(high_score.read())
        self.color('white')            
        self.pu()
        self.goto(0, 270)
        self.print_score()
        self.ht()     
        
    def print_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font = FONT)
    
    def score_up(self):
        self.score += 1
        self.clear()
        self.print_score()
        
    def new_best(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('score.txt', 'w') as high_score:
                high_score.write(str(self.high_score))
            return True
        else:
            return False
        
    def game_over(self):
        if not self.new_best():
            self.goto(0,0)
            self.write('GAME OVER!', align=ALIGNMENT, font = GAME_OVER_FONT) 
            self.goto(0,-30)  
            self.write(f'Your Score: {self.score}', align=ALIGNMENT, font = FONT)
            self.goto(0,-60)  
            self.write(f'Highscore: {self.high_score}', align=ALIGNMENT, font = FONT)
        else:
            self.goto(0,0)
            self.write('NEW BEST!', align=ALIGNMENT, font = GAME_OVER_FONT) 
            self.goto(0,-30)  
            self.write(f'Your Score: {self.score}', align=ALIGNMENT, font = FONT)                    
    
    def current_score(self):
        return self.score