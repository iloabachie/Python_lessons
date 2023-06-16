from random import randint
from turtle import Turtle, Screen


y_positions = [-70, -40, -10, 20, 50, 80, 110]
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
all_turtles = []

screen = Screen()
screen.setup(width=500, height=400)

while True:
    user_bet = screen.textinput(title='Make your bet', prompt='Which turtle wins? Enter colour: ').lower()
    if user_bet in colours:
        break
    print('You chose an invalid turtle colour!!!')

for index in range(7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colours[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)

race_on = True
while race_on:
    for turtle in all_turtles:
        rand_dist = randint(1, 10)
        turtle.forward(rand_dist)
        if turtle.xcor() >= 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win!!! The {winning_color.upper()} turtle is the winner!")
            else:
                print(f"You lost!!! You chose {user_bet.upper()} turtle but {winning_color.upper()} turtle is the winner!")

print('The positions are as follows:')
for _ in range(7):
    print(f'{colours[_]} = {all_turtles[_].xcor()}')               

positions = []
for _ in all_turtles:
    positions.append(_.xcor())
positions.sort(reverse=True)
print()
for p in positions:
    for t in all_turtles:
        if t.xcor() == p:
            pos = positions.index(p) + 1
            print(f'{pos}{"st" if pos == 1 else "nd" if pos == 2 else "rd" if pos == 3 else "th"} position: {t.pencolor()} at {t.xcor()}')
    
    
screen.exitonclick()