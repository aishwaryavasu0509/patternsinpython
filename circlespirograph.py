import turtle
tim=turtle.Turtle()
tim.pensize(2)
tim.speed(20)
tim.shape('turtle')
"""use loop statements to save lines"""
for i in range(6):
    for colours in ['red','violet','black','yellow','magenta','green']:""list of colors to choose from"""
        tim.color(colours)
        tim.circle(100)
        tim.left(10)
turtle.done()
