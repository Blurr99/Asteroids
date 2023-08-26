from turtle import Screen
from shuttle import Shuttle
from asteroids import Asteroids
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=900, width=800)
screen.bgcolor('black')
screen.title('Space Invaders')
screen.tracer(0)

shuttle = Shuttle()
asteroids = Asteroids()
scoreboard = Scoreboard()

screen.update()
screen.listen()
screen.onkey(shuttle.go_left, "Left")
screen.onkey(shuttle.go_right, "Right")
screen.onkey(shuttle.go_up, "Up")
screen.onkey(shuttle.go_down, "Down")

game_is_on = True

while game_is_on:
    scoreboard = Scoreboard()
    time.sleep(0.001)
    screen.update()
    asteroids.create_asteroid()
    shuttle.start_shoot(shuttle)
    shuttle.bullet_move()
    asteroids.move()
    for asteroid in asteroids.all_asteroids:
        if asteroid.distance(shuttle)<20:
            game_is_on = False
            scoreboard.game_over()

        for beam in shuttle.bullets:
            if asteroid.distance(beam)<20:
                asteroid.reset()
                scoreboard.hit()
                asteroids.all_asteroids.remove(asteroid)


    

screen.exitonclick()

