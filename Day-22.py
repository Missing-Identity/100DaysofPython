from turtle import Screen, Turtle
from playground import MainScreen
from paddle import Paddle
from ball import Ball
from score import Score1, Score2

# Initial Setup
screen = Screen()
screen.bgcolor("black")
pong_court = MainScreen()
paddle = Paddle()
ball = Ball()
score1 = Score1()
score2 = Score2()
game_on = True
player_1_score = 0
player_2_score = 0
init_score_counter = 0
tim = Turtle()
tim.penup()
tim.color("white")
tim.ht()

# Print court boundary
pong_court.boundary()

# Print Half-Line
pong_court.half_screen_line()

# Print Initial Score
tim.setposition(-120, 350)
tim.write("0", move=True, font=("Avenir", 44, "bold"), align="center")
tim.setposition(120, 350)
tim.write("0", move=True, font=("Avenir", 44, "bold"), align="center")


# Function for Game Over
def game_over():
    pong_court.clear_court()
    paddle.clear_paddles()
    ball.clear_ball()
    tim.setposition(0, 0)
    tim.color("red")
    tim.write("Game Over!", move=True, font=("Avenir", 44, "bold"), align="center")


# Paddle
screen.tracer(0)
paddle.first_paddle()
paddle.second_paddle()
screen.update()
screen.listen()


# Paddle Controls
def movement():
    screen.onkeypress(paddle.up_1, "w")
    screen.onkeypress(paddle.down_1, "s")
    screen.onkeypress(paddle.up_2, "Up")
    screen.onkeypress(paddle.down_2, "Down")


ball.ball_initial_direction()

# Game on
while game_on:
    movement()
    ball.ball_movement()
    ball.ball_collision_with_walls()
    if ball.distance(paddle.turtles_paddle_2) < 70 and ball.xcor() > 660:
        if init_score_counter == 0:
            init_score_counter += 1
            tim.clear()
        score2.clear_score()
        ball.setheading((180 - ball.heading()))
        player_2_score += 1
        score2.player_2_score(player_2_score)
        score1.player_1_score(player_1_score)
    elif ball.distance(paddle.turtles_paddle_1) < 70 and ball.xcor() < -660:
        if init_score_counter == 0:
            init_score_counter += 1
            tim.clear()
        score1.clear_score()
        ball.setheading((180 - ball.heading()))
        player_1_score += 1
        score1.player_1_score(player_1_score)
        score2.player_2_score(player_2_score)
    elif ball.distance(paddle.turtles_paddle_1) >= 70 and ball.xcor() < -680:
        game_on = False
        game_over()
    elif ball.distance(paddle.turtles_paddle_2) >= 70 and ball.xcor() > 680:
        game_on = False
        game_over()
    screen.update()


# Screen settings
screen.exitonclick()
screen.screensize(700, 440)
