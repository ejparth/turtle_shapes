from random import choice
from turtle import Turtle, Screen

tim = Turtle()
tim.color('red', 'yellow')
angle = 0

color = ["yellow", "blue", "brown"]


def draw(sides,in_color ):
    tim.pencolor(in_color)
    shape_angle = 360 / sides
    for i in range(sides):
        tim.forward(100)
        tim.right(shape_angle)


for i in range(3, 7):
    draw(i, choice(color))

screen = Screen()
screen.exitonclick()
