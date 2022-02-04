from turtle import Turtle

height = 430*2
width = 700*2


class MainScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.pensize(10)
        self.ht()
        self.color("white")

    def half_screen_line(self):
        self.penup()
        self.setposition(0, 430)
        self.setheading(270)
        while self.position()[1] >= -410:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
            print(self.position())

    def boundary(self):
        self.penup()
        self.setposition(-705, -430)
        self.setheading(0)
        self.pendown()
        self.forward(width)
        self.setheading(90)
        self.forward(height)
        self.setheading(180)
        self.forward(width)
        self.setheading(270)
        self.forward(height)

    def clear_court(self):
        self.clear()
