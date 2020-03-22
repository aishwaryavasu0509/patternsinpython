import turtle
tim=turtle.Turtle()
tim.left(90)
tim.speed(150)
def tree(i):
    if i<10:
        return
    else:
        tim.forward(i)
        tim.left(30)
        tree(3*i/4)
        tim.right(60)
        tree(3*i/4)
        tim.left(30)
        tim.backward(i)
tree(100)
turtle.done()

