from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 30, 'bold')


class Score(Turtle):

    def __init__(self, position=(0, 0)):
        
        super().__init__()
        self.end = 'GAME\nOVER'
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.update_score()
        

    def update_score(self):
        self.clear()
        self.goto(-220, 260)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(220, 260)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.clear()
        self.goto(-220, 0)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(220, 0)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        self.goto(0, 50)
        self.write(self.end, align=ALIGNMENT, font=FONT)

    def increase_lscore(self):
        self.l_score += 1
        self.update_score()
    
    def increase_rscore(self):
        self.r_score += 1
        self.update_score()