# coding: utf-8

import turtle
import random
import math

turtle.speed(6)

for i in range(30, 180, 30):
    #turtle.fillcolor(random.random(),random.random(),random.random())
    #turtle.begin_fill()
    turtle.penup()
    turtle.goto(0,-i)
    turtle.pendown()
    turtle.circle(i)
    #turtle.end_fill()

