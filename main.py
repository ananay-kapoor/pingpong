from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time
screen=Screen()
screen.setup(width=1000,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
paddle=Paddle()
ball=Ball()
screen.update()
score=Scoreboard()
is_game_on=True
is_moving=True
def resume_game():
    global is_moving
    is_moving=True
def end_game():
    global is_game_on
    is_game_on = False
loop_count=0
screen.listen()
screen.onkeypress(paddle.move_up_p1,"Up")    
screen.onkeypress(paddle.move_down_p1,"Down")
screen.onkeypress(paddle.move_up_p2,"w")
screen.onkeypress(paddle.move_down_p2,"s")
while is_game_on:
    if loop_count==15:
        is_game_on=False
        score.gameover()
        ball.reset()
        paddle.reset()
    time.sleep(ball.movespeed)
    screen.update()
    if is_moving:
        ball.move()
        for slider in paddle.paddle_list:
            if ball.distance(slider)<50 and ball.xcor()>450 or ball.distance(slider)<50 and ball.xcor()<-450: 
                ball.bounce_x()
        if ball.ycor()>=280 or ball.ycor()<-280:
            ball.bounce_y()
        if ball.xcor()>500:
            is_moving=False
            score.increase_score_left()
            ball.start_again()
            screen.onkey(resume_game,"Return")
            screen.onkey(end_game,"e")
            loop_count+=1
        if ball.xcor()<-500:
            is_moving=False
            score.increase_score_right()
            ball.start_again()
            screen.onkey(resume_game,"Return")
            screen.onkey(end_game,"e")
            loop_count+=1
score.gameover()
ball.reset()
paddle.reset()
screen.exitonclick()