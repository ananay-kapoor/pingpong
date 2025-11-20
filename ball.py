from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape('circle')
        self.color('white')
        self.penup()
        self.movespeed= 0.06
        self.dx=random.choice([10,-10])
        self.dy=random.choice([10,-10])
    def move(self):
        new_x=self.xcor()+self.dx
        new_y=self.ycor()+self.dy
        self.goto(new_x,new_y)
    def bounce_x(self):
        self.dx*=-1
    def bounce_y(self):
        self.dy*=-1
        self.movespeed*=0.9
    def restart(self):
        self.goto(0,0)
        self.movespeed=0.06
    def start_again(self):
        self.restart()

    
        