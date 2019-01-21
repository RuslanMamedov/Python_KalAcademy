# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 13:23:43 2019

@author: Mamedova
"""
#Class Exercises - Variables and Instructions

#get radius from the user

'''import turtle

radius = eval (input ('Enter the radius of the circle: ')) #right to left code style

def DrawCircle (color, x, y, r):  #required parameters first, optional(default) parameters (radius) at the end
    turtle.pensize(5)
    turtle.color(color)
    turtle.penup() #to move pen to a new location
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(r)
    
DrawCircle('blue',-110,-25,radius)
DrawCircle('black',0,-25,radius)
DrawCircle('red',110,-25,radius)
DrawCircle('yellow',-55,-75,radius)
DrawCircle('green',55,-75,radius)'''

assignment = eval(input ('Enter the assignment number:'))

#2.1 Convert Celsius to Fahrenheit
if assignment ==1:
    celsius = eval(input('Enter degrees in Celsius: '))
    fahrenheit = (9 / 5) * celsius + 32 
    print (celsius,'Celsius is',fahrenheit,'Fahrenheit.')

#2.2 Compute the volume of a cylinder
if assignment ==2:
    pi = 3.14
    radius, length = eval (input ('Enter the radius and length of a cylinder: '))
    area = pi*radius**2
    volume = area*length
    print ('The area is',area,'and the volume is',volume,'.')

#2.4 Convert pounds into kilograms
if assignment ==4:
    pounds = eval(input('Enter weight in pounds:'))
    kilograms = 0.453592 * pounds
    print (pounds,' pounds is ',kilograms,' kilograms.')

#2.5 Subtotal and a gratuity rate: 
if assignment ==5:
    subtotal,gratuity = eval(input('Enter the subtotal and a gratuity rate:')) 
    print ('gratuity is',subtotal*gratuity/100,'and total is',subtotal+subtotal*gratuity/100)

