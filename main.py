from nis import match
from time import sleep
from turtle import Screen
from Ball import Ball

from Paddle import Paddle
from Scoreboard import Scoreboard


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()

screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")

right_paddle = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT, position="right")
left_paddle = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT, position="left")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.move_up, key="Up")
screen.onkey(right_paddle.move_down, key="Down")    
screen.onkey(left_paddle.move_up, key="w")
screen.onkey(left_paddle.move_down, key="s")
game_active = True
screen.onkeypress(ball.start_moving)

while game_active:
    sleep(ball.move_speed)
    screen.update()
    if ball.moving:
        ball.move()

    if ball.ycor() > SCREEN_HEIGHT/2 -20 or ball.ycor() < - (SCREEN_HEIGHT/2 -20):
        ball.bounce_y()
       
    if ball.distance(right_paddle) < 60 and ball.xcor() > SCREEN_WIDTH/2 -50 or ball.distance(left_paddle) < 60 and ball.xcor() < -(SCREEN_WIDTH/2 -50) :
        ball.bounce_x()

    if ball.xcor() > SCREEN_WIDTH/2 -20:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < - (SCREEN_WIDTH/2 -20):
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()