from turtle import Turtle
from random import choice, randint
from time import sleep

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10




class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    
    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=3, stretch_wid=1)
            new_car.penup()
            new_car.color(choice(COLORS))
            y_cor = []
            for y in range(-250, 250, 25):
                y_cor.append(y)
            new_car.goto(300, choice(y_cor))
            self.all_cars.append(new_car)
    
    def drive(self):
        for car in self.all_cars:
            car.backward(self.speed)
 
    def level_up(self):
        self.speed += MOVE_INCREMENT
    
