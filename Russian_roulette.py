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

def draw_drum(i):    #Рисует каморы, создает эффект вращения барабана
    angle = phi_rad * i
    gotoxy(math.sin(angle)*r, math.cos(angle)*r + 60)
    draw_circle(22, 'brown')
    draw_circle(22, 'white')
# Закрашивает область с указанными координатами(x,y) белой полосой шириной 60, указанной  длины(z)
def paint_over(x, y, z): 
    gotoxy(x, y)
    turtle.color('white')
    turtle.width(60)
    turtle.forward(z)
    turtle.color('black')
    turtle.width(1)

turtle.speed(0)
gotoxy(-180,300)
turtle.write("Игра: 'РУССКАЯ РУЛЕТКА'", font=("Arial", 30, "normal"))
# Рисуем револьвер
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

phi = 360 / bull_count           #считаем угол в градусах
phi_rad = phi * math.pi / 180.0  #переводим в радианы
r = 50              #радиус по которому будут расположены каморы
# Рисуем каморы
for i in range(0,bull_count):  
    draw_drum(i)
answer = ''
start = 0
turtle.hideturtle() 
while answer != 'N':
    answer = turtle.textinput("Сыграем?", "Y/N")
    # Закрашивает текст(жив, убит) над револьвером, для возможности повторить  не выходя из игры.
    paint_over(-130,250,350)  
    if answer == 'Y':
        for i in range(start,random.randrange(bull_count,100)):    
            draw_drum(i)
                
        draw_circle(22, 'brown')
        
        start = i % bull_count  #определяем положение каморы с пулей
        if start == 0:
            gotoxy(-60,250)
            turtle.write("Tы убит!", font=("Arial", 24, "normal"))
        else:
            gotoxy(-100,250)
            turtle.write("Повезло! Ты жив!", font=("Arial", 24, "normal"))            
        
    else:
        pass
