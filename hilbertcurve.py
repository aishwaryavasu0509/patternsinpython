from turtle import Screen,Turtle
def hilbert_curve(turtle,A,parity,n):
    if n<1:
        return
    turtle.left(parity*90)
    hilbert_curve(turtle, A, -parity, n-1)
    turtle.forward(A)
    turtle.right(parity*90)
    hilbert_curve(turtle, A, parity, n-1)
    turtle.forward(A)
    hilbert_curve(turtle, A, parity, n-1)
    turtle.right(parity*90)
    turtle.forward(A)
    hilbert_curve(turtle, A,- parity, n-1)
    turtle.left(parity*90)
screen=Screen()
yertle=Turtle()
yertle.speed(50)
hilbert_curve(yertle,10,1,4)
screen.exitonclick()
