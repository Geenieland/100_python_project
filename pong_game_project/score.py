from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.dad_score = 0
        self.lucas_score = 0
        self.update_scoreboard()

    def dad_son(self):
        self.dad = "JASON"
        self.son = "LUCAS"
        self.goto(-150,200)
        self.write(self.dad, align="left", font=("Courier", 20, "normal"))
        self.goto(150, 200)
        self.write(self.son, align="right", font=("Courier", 20, "normal"))



    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.dad_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.lucas_score, align="center", font=("Courier", 80, "normal"))

    def dad_point(self):
        self.dad_score += 1
        self.update_scoreboard()

    def lucas_point(self):
        self.lucas_score += 1
        self.update_scoreboard()
