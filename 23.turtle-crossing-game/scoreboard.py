from turtle import Turtle

FONT = ("Courier", 15, "normal")
GAME_OVER_FONT = ("Courier", 30, "bold")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')    
        with open('score.txt', 'r') as file:
            read = file.read()
            hl, hp = read.split()
            self.high_score = [int(hl), int(hp)]
        self.pu()
        self.goto(-220, 260)
        self.print_score()
        self.ht()
       
    def set_high_score(self, progress):
        if self.level > self.high_score[0]:
            self.high_score = [str(self.level), str(progress)]
            with open('score.txt', 'w') as file:
                file.write(str(self.high_score[0]) + ' ' + self.high_score[1])
            return True
        else:
            return False
        
        if self.level == self.high_score[0]:
            if progress > self.high_score[1]:
                self.high_score = [str(self.level), str(progress)]
                with open('score.txt', 'w') as file:
                    file.write(str(self.high_score[0]) + ' ' + self.high_score[1])
                return True
        else:
            return False
           
    def print_score(self):
        self.write(f'Level: {self.level}/30', align=ALIGNMENT, font = FONT)    
        
    def next_level(self):
        self.level += 1
        self.clear()
        self.print_score()

    def game_over(self, progress):
        if not self.set_high_score(progress):
            self.goto(0,0)
            self.write('GAME OVER!', align=ALIGNMENT, font = GAME_OVER_FONT) 
            self.goto(0,-30)  
            self.write(f'Reached level: {self.level}', align=ALIGNMENT, font = FONT)
            self.goto(0,-60)  
            self.write(f'Progress: {progress}%', align=ALIGNMENT, font = FONT)
            self.goto(0,-100)          
            self.write(f'High Score: level {self.high_score[0]}, {self.high_score[1]}%', align=ALIGNMENT, font = FONT)
        else:
            self.goto(0,0)
            self.write('NEW BEST!', align=ALIGNMENT, font = GAME_OVER_FONT) 
            self.goto(0,-30)  
            self.write(f'Reached level: {self.level}', align=ALIGNMENT, font = FONT)
            self.goto(0,-60)  
            self.write(f'Progress: {progress}%', align=ALIGNMENT, font = FONT)