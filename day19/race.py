from random import randint
from turtle import Turtle, Screen


race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle wins? Enter colour: ')
# print(user_bet)

y_positions = [-70, -40, -10, 20, 50, 80, 110]
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
all_turtles = []


for index in range(7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colours[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)
    


if user_bet:
    race_on = True

    while race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You win!!! The {winning_color.upper()} turtle is the winner!")
                else:
                    print(f"You lost!!! You chose {user_bet.upper()} turtle but {winning_color.upper()} turtle is the winner!")
            rand_dist = randint(0, 10)
            turtle.forward(rand_dist)


    screen.exitonclick()
    print(f'The positions are as follows:\n{colours[0]} = {all_turtles[0].xcor()}\n{colours[1]} = {all_turtles[1].xcor()}\n{colours[2]} = {all_turtles[2].xcor()}\n{colours[3]} = {all_turtles[3].xcor()}\n{colours[4]} = {all_turtles[4].xcor()}\n{colours[5]} = {all_turtles[5].xcor()}\n{colours[6]} = {all_turtles[6].xcor()}\n')
else:
    screen.exitonclick()
    print('You did not choose a turtle!!!')