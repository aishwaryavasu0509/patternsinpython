# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 10:51:28 2020

@author: aishw
"""


import turtle
tim=turtle.Turtle()
tim.pensize(2)
tim.speed(20)
tim.shape('turtle')
for i in range(6):
    for colours in ['red','violet','black','yellow','magenta','green']:
        tim.color(colours)
        tim.circle(100)
        tim.left(10)
turtle.done()