
import turtle

turtle.speed(0)

colors = ['red', 'purple', 'blue','green', 'yellow', 'orange']
'''t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x / 100 + 1)
    t.forward(x) 
    t.left(59)'''
    
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(0,150,5):
    t.pencolor(colors[x % 6])
    t.circle(x)
    t.left(181)    


