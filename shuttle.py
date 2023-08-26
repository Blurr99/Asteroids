from turtle import Turtle

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Shuttle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.setheading(90)
        self.penup()
        self.color('white')
        self.goto(0,-420)
        self.bullets = []
        self.bullet_speed = STARTING_MOVE_DISTANCE
        self.bullet_speed_increment = MOVE_INCREMENT

    def go_left(self):
        if self.xcor()>=-350:
            new_x = self.xcor()-20
            self.goto(new_x,self.ycor())

    def go_right(self):
        if self.xcor()<=350:
            new_x = self.xcor()+20
            self.goto(new_x,self.ycor())

    def go_up(self):
        if self.ycor()<=400:
            new_y = self.ycor()+20
            self.goto(self.xcor(),new_y)

    def go_down(self):
        if self.ycor()>=-400:
            new_y = self.ycor()-20
            self.goto(self.xcor(),new_y)

    def start_shoot(self, player):
        bullet = Turtle()
        bullet.shape('square')
        bullet.penup()
        bullet.shapesize(stretch_len=1,stretch_wid=0.05)
        bullet.color('red')
        bullet.goto(player.xcor(),player.ycor()+20)
        bullet.setheading(90)
        self.bullets.append(bullet)
        
    def bullet_move(self):
        for shot in self.bullets:
            shot.forward(self.bullet_speed)


