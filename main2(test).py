from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
screen=Screen()
screen.setup(width=1000,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
paddle=Paddle()
screen.update()
ball=Ball()
is_game_on=True
is_moving=True
def resume_game():
    global is_moving
    is_moving=True
screen.listen()
screen.onkeypress(paddle.move_up_p1,"Up")    
screen.onkeypress(paddle.move_down_p1,"Down")
screen.onkeypress(paddle.move_up_p2,"w")
screen.onkeypress(paddle.move_down_p2,"s")
while is_game_on:
    time.sleep(0.035)
    screen.update()
    if is_moving:
        ball.move()
        for slider in paddle.paddle_list:
            if ball.distance(slider)<50 and ball.xcor()>450 or ball.distance(slider)<50 and ball.xcor()<-450: 
                ball.bounce_x()
        if ball.ycor()>=280 or ball.ycor()<-280:
            ball.bounce_y()
        if ball.xcor()>500 or ball.xcor()<-500:
            is_moving=False
            ball.start_again()
            screen.onkey(resume_game,"Return")
screen.exitonclick()