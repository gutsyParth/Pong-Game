from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.penup()
        self.speed("fastest")
    
    x_mov=2
    y_mov=2

    def mov(self):
        self.goto(self.xcor()+self.x_mov,self.ycor()+self.y_mov)

    
    