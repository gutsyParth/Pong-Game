from turtle import Turtle

class Board(Turtle):
    def __init__(self,cord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(cord[0],cord[1])
        self.speed("fastest")

    def w_up(self):
        self.goto(self.xcor(),self.ycor()+30)

    def s_down(self):
        self.goto(self.xcor(),self.ycor()-30)
    
    def Up_up(self):
        self.goto(self.xcor(),self.ycor()+30)

    def Down_down(self):
        self.goto(self.xcor(),self.ycor()-30)