# coding: utf-8

import turtle
import random
import math

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


turtle.speed(0)

gotoxy(0,0)
turtle.circle(80)
gotoxy(0,160)
draw_circle(5, 'red')

phi = 360 / 7
r = 50

for i in range(0,7):  
    phi_rad = phi * i * math.pi / 180.0
    gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60)     
    draw_circle(22, 'white')
answer = ''
start = 0
while answer != 'N':
    answer = turtle.textinput("Сыграем?", "Y/N")
    if answer == 'Y':
        for i in range(start,8): #random.randrange(7,100)   
            phi_rad = phi * i * math.pi / 180.0
            gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60)
            draw_circle(22, 'brown')
            draw_circle(22, 'white')
        
        
        gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60)
        draw_circle(22, 'brown')
        
        start = i % 7
        if start == 0:
            gotoxy(-60,250)
            turtle.write("Tы убит!", font=("Arial", 24, "normal"))        

    else:
        pass
