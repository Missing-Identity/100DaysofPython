from turtle import Turtle
from random import randint

ball_speed = 7


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.number = randint(0, 360)
        self.penup()

    def ball_initial_direction(self):
        self.setheading(self.number)

    def ball_movement(self):
        self.forward(ball_speed)

    def ball_collision_with_walls(self):
        if 420 < self.position()[1] or self.position()[1] < -420:
            self.set_heading()

    def set_heading(self):
        self.setheading((360 - self.heading()))

    def clear_ball(self):
        self.reset()
