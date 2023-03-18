from turtle import Turtle
from random import choice

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.move_speed = 0.1
        self.x_move = 10 * choice([-1, 1])
        self.y_move = 10 * choice([-1, 1])

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def ybounce(self):
        self.y_move *= -1
    
    def xbounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    
    def reset(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.x_move *= choice([-1, 1])
        self.y_move *= choice([-1, 1])

    def end_ball(self):
        self.clear()

    


        
        