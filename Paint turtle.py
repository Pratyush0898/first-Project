import turtle
from turtle import *
t=Turtle()
wn=Screen()
wn.title("Draw using mouse")
t.pencolor('black')
t.speed(-1)
# ondrag is used to bind this function to mouse event
def paint(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(paint)

def erase(x,y):
    t.clear()
    wn.listen()
    t.ondrag(paint)

def main():
    wn.onscreenclick(erase,3)
    done()

    main()

turtle.done()