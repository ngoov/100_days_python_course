from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from screen import GameScreen
import time

screen = GameScreen()
screen.force_open_on_top()

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320 \
            or ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        left_paddle.reset_position()
        right_paddle.reset_position()
        ball.bounce_x()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        left_paddle.reset_position()
        right_paddle.reset_position()
        ball.bounce_x()
        scoreboard.r_point()




screen.mainloop()