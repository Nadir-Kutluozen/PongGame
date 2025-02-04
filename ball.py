from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10


    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)


    def bounce(self):
        self.y_move *= -1


    def bounce_back(self):
        self.x_move += 2
        self.y_move += 2
        self.x_move *= -1


    def reset_pos(self):
        self.home()