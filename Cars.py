from turtle import Turtle
import random

DISTANCE = []


class Car(Turtle):
    def __init__(self):
        super().__init__()  # constructor

    def many(self):
        LIST = ["red", "blue", "black", "green"]
        self.penup()
        self.goto(250, 0)
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(LIST))
        new_x = random.randint(-230, 230)
        new_y = random.randint(-280, 280)
        DISTANCE.append(self.goto(new_x, new_y))
        return DISTANCE
