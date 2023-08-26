from turtle import Turtle
FONT = ("Courier", 15, "normal")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pencolor('green')
        self.penup()
        self.goto(-350,400)
        self.pendown()
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGN,font= FONT)

    def hit(self):
        self.score += 100
        self.clear()
        self.display_score()
    
    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.pencolor('red')
        self.write(f"GAME OVER! \n Your Score: {self.score}",align=ALIGN,font= FONT)
        