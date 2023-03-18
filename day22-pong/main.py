from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
scores = Score()


def pause_game():  #not working
    global pause
    pause = 5000 
        
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
screen.onkey(pause_game, 'space') # nto working

game_on = True
max_score = 5

while game_on:
    pause = 0
    time.sleep(ball.move_speed)
    # time.sleep(pause)
    # time.sleep(0.001)
    screen.update()
    if pause == True:  #not working
        pause1 = screen.textinput(title='Paused', prompt='Press OK to continue')
    elif scores.r_score == max_score or scores.l_score == max_score:
        game_on = False
        ball.end_ball()
        scores.game_over()
    else:    
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.ybounce()

        # elif ball.xcor() == 400 or ball.xcor() == -400:
        #     ball.xbounce()

        # elif ball.xcor() == -400 and ball.distance(l_paddle) <= 250:
        #     ball.xbounce()
         
        elif ball.distance(l_paddle) <= 60 and ball.xcor() == (l_paddle.xcor() + 20) or ball.distance(r_paddle) <= 60 and ball.xcor() == (r_paddle.xcor() - 20):
            ball.xbounce()
        elif ball.xcor() < -460:
            scores.increase_rscore()
            ball.reset()
        elif ball.xcor() > 460:
            scores.increase_lscore()
            ball.reset()

screen.exitonclick()



import time

