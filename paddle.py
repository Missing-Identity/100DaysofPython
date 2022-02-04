from turtle import Turtle


class Paddle:
    def __init__(self):
        self.turtles_paddle_1 = None
        self.turtles_paddle_2 = None
        self.position_of_x_1 = -680
        self.position_of_y_1 = 40
        self.position_of_x_2 = 670
        self.position_of_y_2 = 40

    def first_paddle(self):
        tim = Turtle("square")
        tim.penup()
        tim.color("red")
        tim.resizemode("user")
        tim.shapesize(stretch_wid=8, stretch_len=1)
        tim.setposition(self.position_of_x_1, self.position_of_y_1)
        self.turtles_paddle_1 = tim

    def second_paddle(self):
        tim = Turtle("square")
        tim.penup()
        tim.color("red")
        tim.resizemode("user")
        tim.shapesize(stretch_wid=8, stretch_len=1)
        tim.setposition(self.position_of_x_2, self.position_of_y_2)
        self.turtles_paddle_2 = tim

    def up_1(self):
        if 340 > self.turtles_paddle_1.position()[1]:
            self.turtles_paddle_1.setposition(self.turtles_paddle_1.position()[0],
                                              (self.turtles_paddle_1.position()[1] + 40))
        else:
            pass

    def down_1(self):
        if self.turtles_paddle_1.position()[1] > -325:
            self.turtles_paddle_1.setposition(self.turtles_paddle_1.position()[0], (self.turtles_paddle_1.position()[1]-40))
        else:
            pass

    def up_2(self):
        if 340 > self.turtles_paddle_2.position()[1]:
            self.turtles_paddle_2.setposition(self.turtles_paddle_2.position()[0],
                                              (self.turtles_paddle_2.position()[1] + 40))
        else:
            pass

    def down_2(self):
        if self.turtles_paddle_2.position()[1] > -325:
            self.turtles_paddle_2.setposition(self.turtles_paddle_2.position()[0], (self.turtles_paddle_2.position()[1]-40))
        else:
            pass

    def clear_paddles(self):
        self.turtles_paddle_1.reset()
        self.turtles_paddle_2.reset()

    # def first_paddle(self):
    #     for i in range(0, 7):
    #         tim = Turtle("square")
    #         tim.penup()
    #         tim.color("red")
    #         tim.speed("fastest")
    #         tim.setposition(self.position_of_x_1, self.position_of_y_1)
    #         self.turtles_paddle_1.append(tim)
    #         self.position_of_y_1 -= 20
    #
    # def second_paddle(self):
    #     for i in range(0, 7):
    #         tim = Turtle("square")
    #         tim.penup()
    #         tim.color("red")
    #         tim.speed("fastest")
    #         tim.setposition(self.position_of_x_2, self.position_of_y_2)
    #         self.turtles_paddle_2.append(tim)
    #         self.position_of_y_2 -= 20
    #
    # def up_1(self):
    #     for pad in self.turtles_paddle_1:
    #         if 400 > pad.position()[1]:
    #             pad.setheading(90)
    #             pad.forward(40)
    #         else:
    #             break
    #
    # def down_1(self):
    #     for pad in self.turtles_paddle_1:
    #         if self.turtles_paddle_1[6].position()[1] > -400:
    #             pad.setheading(270)
    #             pad.forward(40)
    #         else:
    #             break
    #
    # def up_2(self):
    #     for pad in self.turtles_paddle_2:
    #         if 400 > pad.position()[1]:
    #             pad.setheading(90)
    #             pad.forward(40)
    #         else:
    #             break
    #
    # def down_2(self):
    #     for pad in self.turtles_paddle_2:
    #         if self.turtles_paddle_2[6].position()[1] > -400:
    #             pad.setheading(270)
    #             pad.forward(40)
    #         else:
    #             break
