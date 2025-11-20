from turtle import Turtle
FONT='Courier'
POSITIONS=[(-480,280),(480,280),(0,0),(0,-60)]
class Scoreboard():
    def __init__(self):
        self.score_list=[]
        self.score_left=0
        self.score_right=0
        self.scoreboard()
    def scoreboard(self):
        for position in POSITIONS:
            score=Turtle()
            score.hideturtle()
            score.penup()
            score.color('white')
            score.goto(position)
            self.score_list.append(score)
        self.update_left()
        self.update_right()
    def update_left(self,):
        self.score_list[0].clear()
        self.score_list[0].write(f"Score:{self.score_left}",False,"left",(FONT,15,"normal"))
    def update_right(self,):
        self.score_list[1].clear()
        self.score_list[1].write(f"Score:{self.score_right}",False,"right",(FONT,15,"normal"))
    def increase_score_left(self):
        self.score_left+=1
        self.update_left()
    def increase_score_right(self):
        self.score_right+=1
        self.update_right()
    def gameover(self):
        self.score_list[2].write("GAME OVER", align="center", font=(FONT, 30, "bold"))
        if self.score_left>self.score_right:    
            self.score_list[3].write("Player 1 Won! \U00002B05", align="center", font=(FONT, 15, "bold"))
        elif self.score_left<self.score_right:
             self.score_list[3].write("Player 2 Won! \U000027A1", align="center", font=(FONT, 15, "bold"))
        else:
            self.score_list[3].write("It's a Draw", align="center", font=(FONT, 15, "bold"))