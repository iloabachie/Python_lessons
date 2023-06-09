from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class Score(Turtle):
    def __init__(self):        
        super().__init__()
        # global high
        self.score = 0
        try:
            with open('./day20-snake/high_score.txt') as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            file = open('./day20-snake/high_score.txt', mode='w')
            file.close()
            self.high_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)
        
    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f'GAME OVER!!!\nYour score: {self.score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('.\day20-snake\high_score.txt', mode='w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()