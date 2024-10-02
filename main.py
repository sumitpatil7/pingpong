from turtle import Turtle, Screen
from paddle import Paddle
from ball import Pongball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("pong")
screen.listen()
screen.tracer(0)

paddy_right = Paddle(350, 0)
paddy_left = Paddle(-350, 0)
ball = Pongball()
scoreboard = Scoreboard()
screen.onkey(paddy_right.move_up, "Up")
screen.onkey(paddy_right.move_down, "Down")
screen.onkey(paddy_left.move_up, "w")
screen.onkey(paddy_left.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # To detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect the contact with the paddle
    if ball.distance(paddy_right) < 50 and ball.xcor() > 320 or ball.distance(paddy_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
