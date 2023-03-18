from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def front():
    tim.forward(25)

def back():
    tim.back(25)

def clock():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def anticlock():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    


screen.listen()

screen.onkey(key='w', fun=front)
screen.onkey(key='s', fun=back)
screen.onkey(key='a', fun=clock)
screen.onkey(key='d', fun=anticlock)
screen.onkey(key='c', fun=clear)

screen.exitonclick()