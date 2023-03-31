from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.end = 'GAME\nOVER'
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_level()
    
    def update_level(self):
        self.clear()
        self.goto(-260, 260)
        self.write(f'Level: {self.level}', font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'Level: {self.level}', font=FONT)
        self.goto(0, 50)
        self.write(self.end, font=FONT)