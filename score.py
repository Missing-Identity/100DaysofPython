from turtle import Turtle


class Score1(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()

    def player_1_score(self, p1):
        self.setposition(-120, 350)
        self.write(f"{p1}", move=True, font=("Avenir", 44, "bold"), align="center")

    def clear_score(self):
        self.clear()


class Score2(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()

    def player_2_score(self, p2):
        self.setposition(120, 350)
        self.write(f"{p2}", move=True, font=("Avenir", 44, "bold"), align="center")

    def clear_score(self):
        self.clear()
