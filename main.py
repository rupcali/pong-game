# pong game project
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
game_over = False

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while not game_over:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # detect collision with paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() == 330 or ball.distance(l_paddle) < 60 and ball.xcor() == -330:
        ball.bounce_x()
        
    # detect when paddle misses left paddle
    if ball.xcor() < -380:
        scoreboard.r_point()
        time.sleep(1)
        ball.reset_position()
        
    # detect when paddle misses right paddle
    if ball.xcor() > 380:
        scoreboard.l_point()
        time.sleep(1)
        ball.reset_position()
        
screen.exitonclick()
