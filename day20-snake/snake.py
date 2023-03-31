from turtle import Turtle


START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)
            
    def add_segment(self, position):
        new_seg = Turtle('square')
        new_seg.color('white')
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def snake_reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)# investigate why the clear() does not work here
            seg.hideturtle()  #can either hide turtle or go to off screen position
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    
    def grow(self):
        '''Increase snake length as it feeds'''
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)   

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

