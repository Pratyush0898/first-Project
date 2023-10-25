import turtle

screen = turtle.Screen()
screen.setup(800,800)
screen.setworldcoordinates(-8,-8,8,8)
screen.tracer(0,0)
screen.title('Bulge Illusion - #python4fun')
turtle.hideturtle()
turtle.speed(0)

color1 = 'light sky blue'
color2 = 'firebrick'
screen.bgcolor(color2)

def draw_square(x,y,size,c):
    turtle.up()
    turtle.goto(x-size/2,y-size/2)
    turtle.seth(0)
    turtle.color(c)
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(size)
        turtle.left(90)
    turtle.end_fill()
    
def draw_board():
    for x in range(-7,8,2):
        for y in range(-7,8,2):
            draw_square(x,y,1,color1)
    for x in range(-6,8,2):
        for y in range(-6,8,2):
            draw_square(x,y,1,color1)
            

def draw_diag(x,y):
    c = color2 if (x+y)%2 == 0 else color1
    if x*y > 0:
        draw_square(x-0.3,y+0.3,0.3,c)
        draw_square(x+0.3,y-0.3,0.3,c)
    elif x*y < 0:
        draw_square(x+0.3,y+0.3,0.3,c)
        draw_square(x-0.3,y-0.3,0.3,c)

def draw_straight(x,y):
    c = color2 if (x+y)%2 == 0 else color1
    if y>0:
        draw_square(x-0.3,y-0.3,0.3,c)
        draw_square(x+0.3,y-0.3,0.3,c)
    elif y<0:
        draw_square(x-0.3,y+0.3,0.3,c)
        draw_square(x+0.3,y+0.3,0.3,c)
    elif x>0:
        draw_square(x-0.3,y-0.3,0.3,c)
        draw_square(x-0.3,y+0.3,0.3,c)
    elif x<0:
        draw_square(x+0.3,y-0.3,0.3,c)
        draw_square(x+0.3,y+0.3,0.3,c)
        
def draw_bulge():
    for x in range(-6,7):
        for y in range(-6,7):
            if abs(x)+abs(y)<=7:
                draw_diag(x,y)
                if x==0 or y==0: draw_straight(x,y)
    x,y = -5,-3
    for i in range(3):
        draw_diag(x,y)
        draw_diag(-x,-y)
        draw_diag(x,-y)
        draw_diag(-x,y)
        x += 1
        y -= 1
draw_board()
draw_bulge()
screen.update()


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
