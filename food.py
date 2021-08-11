from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')

    def refresh(self):
        # random_x = random.randint(-280, 280)
        # random_y = random.randint(-280, 280)
        x = [x for x in range(-280, 281, 20)]
        y = [x for x in range(-280, 281, 20)]
        random_x = random.choice(x)
        random_y = random.choice(y)
        self.goto(random_x, random_y)
