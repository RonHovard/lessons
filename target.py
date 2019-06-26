# coding: utf-8

import turtle
import random
import math

def gotoxy(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

turtle.speed(0)

for i in range(265, 10, -30):
    gotoxy(0,-i)
    turtle.fillcolor(random.random(),random.random(),random.random())
    turtle.begin_fill()
    turtle.circle(i)
    turtle.end_fill()

turtle.textinput("TARGET", "")
