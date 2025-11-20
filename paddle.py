from turtle import Turtle
STARTING_POSITIONS=[(470,0),(-470,0)]
UP=90
DOWN=270
class Paddle:
    def __init__(self):
        self.paddle_list=[]
        self.left= 0
        self.right= 0
        self.create_paddles()
    def create_paddles(self):
        for position in STARTING_POSITIONS:
            paddle=Turtle('square')
            paddle.penup()
            paddle.color('white')
            paddle.shapesize(stretch_wid=1,stretch_len=5)
            paddle.setheading(90)
            paddle.speed(0)
            paddle.goto(position)
            self.paddle_list.append(paddle)
    def move_up_p1(self):
        if self.paddle_list[0].ycor()<240:
            new_y=self.paddle_list[0].ycor()+20
            self.paddle_list[0].goto(self.paddle_list[0].xcor(),new_y)
        else:
            pass
    def move_up_p2(self):
        if self.paddle_list[1].ycor()<240:
            self.paddle_list[1].fd(20)
        else:
            pass
    def move_down_p1(self):
        if self.paddle_list[0].ycor()>-240:
            self.paddle_list[0].bk(20)
        else:
            pass
    def move_down_p2(self):
        if self.paddle_list[1].ycor()>-240:
            self.paddle_list[1].bk(20)
        else:
            pass
    def reset(self):
        for paddle in self.paddle_list:
            paddle.reset()