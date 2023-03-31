from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=10, stretch_wid=10)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()
    

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
