import matplotlib
from prettytable import PrettyTable
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('green')
timmy.forward(100)
my_screen = Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()


table = PrettyTable()
table.add_column('naiime', ['ewerer', 'rtwerertr', '325435345'])
table.add_column('name', ['ererer', 'rtwertwer', '323524345'])
table.add_column('hnnnn', ['erewer', 'rtwertwertr', '32543525'])

table.align = 'r'
print(table)


class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print('my name is ' + self.name)
        print('my name is ' + self.color)
        print(f'my name is {self.weight}')


r1 = Robot('tom', 'red', 34)
r1.introduce_self()


class Polygon():
    def __init__(self, sides, name, size=50):
        self.sides = sides
        self.name = name
        self.size = size
        self.angle = 180-(((sides - 2)*180)/sides)

    def draw(self):
        import turtle
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(self.angle)

        turtle.done()


# shape1 = Polygon(4, 'square')
# print(shape1.name)
# print(shape1.angle)
# shape1.draw()


shape2 = Polygon(70, 'sixagon', 20)
print(shape2.name)
print(shape2.angle)
shape2.draw()
