from turtle import *

######## EX1 ########

def ex1():
    for i in range(3):
        forward(100)
        right(120)

#Appel de la fonction
'''ex1()''' 

######## EX2 ########

def ex2():
    for i in range(4):
        forward(100)
        right(90)

#Appel de la fonction
'''ex2()'''

######## EX3 ########

def tracer_carre(l):
     for i in range(4):
         forward(l)
         right(90)

#Appel de la fonction
'''tracer_carre(45)
tracer_carre(200)'''

######## EX4 ########

def tracer_polygone(l,nb_cotes):
    for i in range(nb_cotes):
        forward(l)
        right(90)

#Appel de la fonction
'''tracer_polygone(100,5)'''

######## EX5 ########
'''
for i in range(3):
    forward(50)
    left(60)
    forward(50)
    right(120)
    forward(50)
    left(60)
    forward(50)
    right(120)
'''
######## EX6 ########

def koch_1(l):
    forward(l)
    left(60)
    forward(l)
    right(120)
    forward(l)
    left(60)
    forward(l)
    right(120)

#Appel de la fonction
'''koch_1(50)'''

######## EX7 ########

def koch(n,l):
    if n == 0:
        forward(l)
    else:
        for angle in [60,-120,60,0]:
            koch(n-1,l/3)
            left(angle)

#Appel de la fonction
'''
speed(0) 
hideturtle() 
for i in range(5):
    penup()
    goto(0, -100 + 70 * i)
    pendown()
    koch(i,300)
done()
'''

######## EX8 ########
def floch(n,l):
  for i in range(3):
    koch(n,l)
    right(120)
    
'''
speed(0)
hideturtle()
penup()
goto(0,-100)
pendown()
floch(4, 300)
done()
'''

######## EX9 ########

def koch_var(x1,y1,x2,y2):
    distance=((x2-x1)**2 + (y2-y1)**2)**0.5
    if distance<10:
        up()
        goto(x1,y1)
        down()
        goto(x2,y2)
        return
    up()
    goto(x1,y1)
    direction=towards(x2,y2)
    seth(direction)
    fd(distance/3)
    x3,y3 = xcor(), ycor()
    left(90)
    fd(distance/3)
    x4,y4 = xcor(), ycor()
    right(90)
    fd(distance/3)
    x5,y5 = xcor(), ycor()
    right(90)
    fd(distance/3)
    x6,y6 = xcor(), ycor()
    koch_var(x1,y1,x3,y3)
    koch_var(x3,y3,x4,y4)
    koch_var(x4,y4,x5,y5)
    koch_var(x5,y5,x6,y6)
    koch_var(x6,y6,x2,y2)

#Appel de la fonction
'''
koch_var(-400,-400,-400,400)
koch_var(-400,400,400,400)
koch_var(400,400,400,-400)
koch_var(400,-400,-400,-400)
'''
