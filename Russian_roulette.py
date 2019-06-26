# coding: utf-8

import turtle
import random
import math

def gotoxy(x, y):               # перемещает курсор не оставляя линий
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
def draw_circle(r, color):   # рисует круг заданного цвета
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

def draw_drum(i):    #Рисует гнёзда в виде анимации
    angle = phi_rad * i
    gotoxy(math.sin(angle)*r, math.cos(angle)*r + 60)
    draw_circle(22, 'brown')
    draw_circle(22, 'white')

turtle.speed(0)
gotoxy(-170,300)
turtle.write("Игра: 'РУССКАЯ РУЛЕТКА'", font=("Arial", 30, "normal"))

gotoxy(0,0)
turtle.circle(80)
gotoxy(0,160)
draw_circle(5, 'red')
gotoxy(0,-90)
draw_circle(45, 'grey')
gotoxy(0,-180)
draw_circle(45, 'grey')

bull_count = turtle.textinput("Введи кол-во гнёзд.", "не больше 7")
bull_count = int(bull_count)

phi = 360 / bull_count
phi_rad = phi * math.pi / 180.0
r = 50

for i in range(0,bull_count):  
    draw_drum(i)
answer = ''
start = 0
while answer != 'N':
    answer = turtle.textinput("Сыграем?", "Y/N")
    if answer == 'Y':
        for i in range(start,random.randrange(bull_count,100)):    
            draw_drum(i)
                
        draw_circle(22, 'brown')
        
        start = i % bull_count
        if start == 0:
            gotoxy(-60,250)
            turtle.write("Tы убит!", font=("Arial", 24, "normal")) 
        
    else:
        pass
