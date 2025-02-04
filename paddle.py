from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x):
        super().__init__()
        self.penup()
        self.goto(x, 0)
        self.shapesize(1, 5)
        self.setheading(90)
        self.speed("fastest")
        self.color("white")
        self.shape("square")

    def up(self):
        self.forward(50)

    def down(self):
        self.backward(50)

