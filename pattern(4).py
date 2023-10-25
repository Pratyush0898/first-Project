import turtle
turtle.speed(1)
turtle.setup(1000,1000)
turtle.title('Penrose Triangle - #python4fun')

def draw_penrose_triangle(x,y,size,tilt):
    turtle.pencolor((0.2,0.2,0.2))
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(tilt)
    turtle.down()
    turtle.fd(size*2)
    p1x = turtle.xcor()
    p1y = turtle.ycor()
    p1a = turtle.heading()
    turtle.left(120)
    turtle.fd(size*2)
    p2x = turtle.xcor()
    p2y = turtle.ycor()
    p2a = turtle.heading()
    turtle.left(120)
    turtle.fd(size*2)
    p3x = turtle.xcor()
    p3y = turtle.ycor()
    p3a = turtle.heading()
    # gray
    turtle.up()
    turtle.goto(p1x,p1y)
    turtle.seth(p1a)
    turtle.down()
    turtle.fillcolor('dark gray')
    turtle.begin_fill()
    turtle.fd(size)
    turtle.left(120)
    turtle.fd(size*5)
    turtle.left(120)
    turtle.fd(size*6)
    turtle.left(60)
    turtle.fd(size)
    turtle.left(120)
    turtle.fd(size*5)
    turtle.right(120)
    turtle.fd(3*size)
    turtle.end_fill()
    #black
    turtle.up()
    turtle.goto(p2x,p2y)
    turtle.seth(p2a)
    turtle.down()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.fd(size)
    turtle.left(120)
    turtle.fd(5*size)
    turtle.left(120)
    turtle.fd(6*size)
    turtle.left(60)
    turtle.fd(size)
    turtle.left(120)
    turtle.fd(5*size)
    turtle.right(120)
    turtle.fd(3*size)
    turtle.end_fill()
    #white
    turtle.up()
    turtle.goto(p3x,p3y)
    turtle.seth(p3a)
    turtle.down()
    turtle.fd(size)
    turtle.left(120)
    turtle.fd(5*size)
    turtle.left(120)
    turtle.fd(6*size)
    turtle.left(60)
    turtle.fd(size)
    turtle.left(120)
    turtle.fd(5*size)
    turtle.right(120)
    turtle.fd(3*size)

draw_penrose_triangle(-80,-50,80,0)


### This will create .eps file ####
import turtle
from tkinter import *
from turtle import *
from PIL import Image
import os
import time

# keeping eps file name as image
eps_file = "temp.eps"

# generating eps file
ts = turtle.getscreen()
turtle.hideturtle()
ts.getcanvas().postscript(file=eps_file)

# get current python file name as string without ".py"
fname = os.path.basename(__file__)
filename = fname.replace('.py','.png')

# Converting eps file to jpg | with filename 
#im.save(str(filename)+".jpg", "JPEG")

# Convert eps to transparent png using ghost script
os.popen("gswin64c -dSAFER -dBATCH -dNOPAUSE -r300 -sDEVICE=pngalpha -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -sOutputFile="+filename+" -dEPSCrop temp.eps")

# Merge transparent png on top of given background png
time.sleep(2)

# Get transparent image file height / width
img = Image.open(filename)
h, w = img.size
print(h,w)
print("Click on the Turtle Screen To Close")

ts.exitonclick()