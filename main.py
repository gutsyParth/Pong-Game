from turtle import Screen, Turtle
from board import Board
from ball import Ball
import time
screen=Screen()
screen.listen()
screen.bgcolor("black")
screen.setup(width=500,height=500)
screen.tracer(0)

board1=Board((220,0))
board2=Board((-220,0))
ball=Ball()


score2=Turtle()
s2=0
score2.color("white")
score2.penup()
score2.goto(-125,230)


score1=Turtle()
s1=0
score1.color("white")
score1.penup()
score1.goto(125,230)

score2.hideturtle()
score1.hideturtle()

game_is_on=True

game_over=Turtle()
game_over.hideturtle()

def collision():
    global s1
    global s2

    if ball.xcor()>210 or ball.xcor()<-210:
        screen.clear()
    
        if s1>s2:
            game_over.write(f"Game Over !\nPlayer 1: {s1} Player 2: {s2}\nPlayer 1 won !",align="center",font=(20))
        elif s2>s1:
            game_over.write(f"Game Over !\nPlayer 1: {s1} Player 2: {s2}\nPlayer 2 won !",align="center",font=(20))
        else:
            game_over.write(f"Game Over !\nPlayer 1: {s1} Player 2: {s2}\nIt's a tie !",align="center",font=(20))

        
        

    if (ball.xcor()>=200 and ball.distance(board1)<=50):
        s1=s1+1
        ball.x_mov=-1*ball.x_mov
    
    if (ball.xcor()<=-200 and ball.distance(board2)<=50):
        s2=s2+1
        ball.x_mov=-1*ball.x_mov

    if ball.ycor()>=230 or ball.ycor()<=-230:
        ball.y_mov=-1*ball.y_mov


def score_update():
    score2.clear()
    score2.write(f"Player 2 Score : {s2}",align="center",font=(10))
    score1.clear()
    score1.write(f"Player 1 Score : {s1}",align="center",font=(10))



while game_is_on:
    time.sleep(0.01)
    score_update()
    collision()
    ball.mov()    
    screen.onkey(board2.w_up,"w")
    screen.onkey(board2.s_down,"s")
    screen.onkey(board1.Up_up,"Up")
    screen.onkey(board1.Down_down,"Down")
    screen.update()
    

screen.exitonclick()


