# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 06:52:13 2019

@author: Mamedova
"""
#Class Exercises
import turtle

def DrawCircle (color, x, y, radius = 45):  #required parameters first, optional(default) parameters (radius) at the end
    turtle.pensize(5)
    turtle.color(color)
    turtle.penup() #to move pen to a new location
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(radius)
    
DrawCircle('blue',-110,-25)
DrawCircle('black',0,-25)
DrawCircle('red',110,-25)
DrawCircle('yellow',-55,-75)
DrawCircle('green',55,-75)

#1.1
print ('Welcome to Python')
print ('Welcome to Computer Science')
print ('Programming is fun \n')

#1.2
for i in range (0,5):
    print ('Welcome to Python')

#1.3
print ('FFFFFFF   U      U  NN     NN')
print ('FF        U      U  NNN    NN')
print ('FFFFFFF   U      U  NNNN   NN')
print ('FF        U      U  NN  N  NN')
print ('FF         U    U   NN   N NN')
print ('FF          UUUU    NN    NNN')


#1.12
turtle.pensize (5)
turtle.color ('green')
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
for i in range (0,4):
    turtle.forward(200)
    turtle.right(90)
    
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.right(90)
turtle.forward(200)

turtle.penup()
turtle.goto(-100,0)
turtle.left(90)
turtle.pendown()
turtle.forward(200)

#1.13
turtle.color ('blue')
turtle.penup()
turtle.goto(-100,0)
turtle.left(90)
turtle.pendown()
turtle.forward(200)

