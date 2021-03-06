# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:32:20 2020

@author: aishw
"""


import turtle

def turn(i):
    left = (((i & -i) << 1) & i) != 0
    return 'L' if left else 'R'

def curve(iteration):
    return ''.join([turn(i + 1) for i in range(2 ** iteration - 1)])

if __name__ == '__main__':
    turtle.hideturtle()
    turtle.speed(100)
    i = 1
    while True:
        if turn(i) == 'L':
            turtle.circle(-4, 90, 36)
        else:
            turtle.circle(4, 90, 36)
        i += 1