from turtle import Turtle


class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 480)
        self.write(f"scores : {self.score} ", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
