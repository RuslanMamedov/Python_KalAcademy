# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 06:52:13 2019

@author: Mamedova
"""
#Class Exercises
import turtle

turtle.pensize(5)
turtle.color('blue')
turtle.penup() #to move pen to a new location
turtle.goto(-110,-25)
turtle.pendown()
turtle.circle(45)

turtle.pensize(5)
turtle.color('black')
turtle.penup() #to move pen to a new location
turtle.goto(0,-25)
turtle.pendown()
turtle.circle(45)

turtle.pensize(5)
turtle.color('red')
turtle.penup() #to move pen to a new location
turtle.goto(110,-25)
turtle.pendown()
turtle.circle(45)

turtle.pensize(5)
turtle.color('yellow')
turtle.penup() #to move pen to a new location
turtle.goto(-55,-75)
turtle.pendown()
turtle.circle(45)

turtle.pensize(5)
turtle.color('green')
turtle.penup() #to move pen to a new location
turtle.goto(55,-75)
turtle.pendown()
turtle.circle(45)

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

