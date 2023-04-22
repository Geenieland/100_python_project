import time
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


ball = Ball((0,0))
score = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    score.dad_son()
    time.sleep(ball.move_speed)
    ball.move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    #Detect collision with a paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.x_bounce()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        score.dad_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.lucas_point()




screen.exitonclick()
