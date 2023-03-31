from time import sleep
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Cross')
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')

game_is_on = True
while game_is_on:
    sleep(0.1)
    
    car.create_car()
    car.drive()
    screen.update()

    for _ in car.all_cars:
        if _.distance(player) <= 20:
            score.game_over()
            game_is_on = False

        elif player.ycor() > FINISH_LINE_Y:
            player.reset()
            score.level += 1
            car.level_up()
            score.update_level()


screen.exitonclick()