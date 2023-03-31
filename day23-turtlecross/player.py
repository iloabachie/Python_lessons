from turtle import Turtle


STARTING_POSITION = (-100, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.reset()
        

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y != -280:
            self.goto(self.xcor(), new_y)    

    def reset(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
