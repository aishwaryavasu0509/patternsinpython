# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import turtle
def sierpinskistriangle(length,depth):
    if depth>1: turtle.dot()
    if depth==0:
        turtle.stamp()
    else:
        
        turtle.speed(100)
        turtle.forward(length)
        sierpinskistriangle(length/2,depth-1)
        turtle.backward(length)
        turtle.left(120)
        turtle.forward(length)
        sierpinskistriangle(length/2,depth-1)
        turtle.backward(length)
        turtle.left(120)
        turtle.forward(length)
        sierpinskistriangle(length/2,depth-1)
        turtle.backward(length)
        turtle.left(120)
def main():
    length=int(input('enter the length of the side'))
    depth=int(input('enter the depth of the triangle'))
    sierpinskistriangle(length,depth)
    turtle.done()
main()
    
        
        
        
        
  