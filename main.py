from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

from scoreboard import ScoreBoard

game_is_on = True
#creating turtle object
turtle = Turtle()
#creating the screen
screen = Screen()
screen.tracer(0)
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(800,600)
screen.listen()
#creating the paddle object
right_player = Paddle(350)
left_player = Paddle(-350)

#creating ball obj
ball = Ball()
screen.onkey(right_player.up,"Up")
screen.onkey(right_player.down,"Down")
screen.onkey(left_player.up,"w")
screen.onkey(left_player.down,"s")
right_score = ScoreBoard(220)
left_score = ScoreBoard(-220)



while game_is_on:
    time.sleep(1/25)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()
    #deteced collision
    if ball.distance(right_player) < 50 and ball.xcor() > 320 or ball.distance(left_player) < 50 and ball.xcor() < -320:
        ball.bounce_back()
    #collision again

    if ball.xcor() >= 380:
        left_score.update_score()
        ball.reset_pos()
        ball.bounce_back()
    if ball.xcor() < -380:
        right_score.update_score()
        ball.reset_pos()
        ball.bounce_back()












screen.exitonclick()
