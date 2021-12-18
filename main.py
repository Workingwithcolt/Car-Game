from Cars import Car
from turtle import Turtle
from turtle import Screen
import time
screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=500)
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.left(90)
tim.penup()
tim.goto(0, -280)
tim.forward(20)


def movef():
    tim.goto(0, tim.ycor() + 10)


screen.listen()
screen.onkey(key="space", fun=movef)
v = []
is_true = True
car = Car()
for i in range(0,10):
    car.many()
for i in range(0, 10):
    for i in range(0,len(v)):
        for j in v:
            time.sleep(0.02)
            x = j.xcor() - 10
            y = j.ycor()
            j.goto(x, y)
            screen.update()

while is_true:
    screen.update()
screen.exitonclick()

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
