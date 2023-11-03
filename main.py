from turtle import Screen
from paddle import Paddle
from circle import Circle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

score = Scoreboard()

number = 0.1
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
circle = Circle()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_is_over = False
while not game_is_over:
    time.sleep(number)
    screen.update()
    circle.move()

    # Detect collision with wall
    if circle.ycor() > 280 or circle.ycor() < - 280:
        circle.bounce_y()

    # Detect collision with paddle
    if circle.distance(r_paddle) < 50 and circle.xcor() > 320 \
            or circle.distance(l_paddle) < 50 and circle.xcor() < -320:
        circle.bounce_x()
        number /= 1.5
        time.sleep(number)

    if circle.xcor() > 380:
        score.l_point()
        circle.get_out()
        number = 0.1

    if circle.xcor() < -380:
        score.r_point()
        circle.get_out()
        number = 0.1

screen.exitonclick()
