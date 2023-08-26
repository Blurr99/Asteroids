from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Asteroids(Turtle):
    def __init__(self):
        super().__init__()
        self.all_asteroids = []
        self.asteroid_speed = STARTING_MOVE_DISTANCE
        self.asteroid_speed_increment = MOVE_INCREMENT

    def create_asteroid(self):
        random_chance = random.randint(1,12)
        if random_chance == 6:
            new_asteroid = Turtle()
            new_asteroid.shape('circle')
            new_asteroid.penup()
            new_asteroid.color('white')
            x = random.randint(-350,350)
            new_asteroid.goto(x,445)
            new_asteroid.setheading(270)
            self.all_asteroids.append(new_asteroid)
        
    def move(self):
        for asteroid in self.all_asteroids:
            asteroid.forward(self.asteroid_speed)