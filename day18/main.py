# from turtle import Turtle, Screen
import turtle as t
from random import *
# from turtle import Turtle, Screen

timmy = t.Turtle()
t.colormode(255)

# cool star filled drawing
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

timmy.pensize(10)
timmy.speed('fastest')


def rand_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colour = (r, g, b)
    return colour


for sides in range(3, 10):
    # timmy.color(10, 10, 10)
    for _ in range(sides):
        timmy.color(rand_color())
        print(rand_color())
        angle = 360 / sides
        timmy.forward(100)
        timmy.right(angle)


jimmy = t.Turtle()
jimmy.speed('fastest')


def draw_spir(gap):
    for y in range(int(360 / gap)):
        jimmy.color(rand_color())
        jimmy.circle(100)
        jimmy.setheading(jimmy.heading() + gap)


draw_spir(7)

screen = t.Screen()
screen.exitonclick()


