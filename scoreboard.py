from turtle import Turtle
class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(position,200)
        self.color("white")
        self.write(f"{self.score}", False, "right", ("Pixel,", 50, "bold"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", False, "right", ("Pixel,", 50, "bold"))



