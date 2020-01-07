from tkinter import *
import random


master= Tk()
canvas_width = 800
canvas_height = 600

w = Canvas(master, width = canvas_width, height = canvas_height)
w.pack()

def stvorec(x,y,width, height):
    w.create_rectangle(x-width/2,y+height/2, x+width/2, y-height/2)

def stvorec2(x,y,width,height, space, num):
    if(x-width/2>0 and x+width/2<canvas_width and y-height/2>0 and y+height/2<canvas_height):
        for i in range(num):
            stvorec(x,y,width-i*space*2, height-i*space*2)
        return True
    else:
        return False
x =0

while(x<=10):
    n = random.randint(5,10)
    xko = random.randint(0,800)
    yko = random.randint(0,600)
    h = random.randint(150,300)
    j = random.randint(150,300)
    medz  =random.randint(5,10)
    if(stvorec2(xko,yko,h,j,medz,n)==True):
        x+=1
    
