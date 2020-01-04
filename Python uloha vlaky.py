from tkinter import *
import random
master= Tk()
canvas_width = 800
canvas_height = 600

w = Canvas(master, width = canvas_width, height = canvas_height)#
w.pack()

def vagon(x,y,farba):
    w.create_rectangle(x,y,x+100,y+50,fill=farba)
    w.create_line(x,y+40,x-10,y+40,width="3")
    w.create_line(x+100,y+40,x+110,y+40,width="3")
    w.create_oval(x+20,y+40,x+40,y+60,fill="black")
    w.create_oval(x+60,y+40,x+80,y+60,fill="black")


r=50
    
for i in range (4):
    vagon(r,50,"red")
    r=r+120


vagon(50,200,"green")
vagon(170,200,"green")

vagon(50,350,"blue")
vagon(170,350,"blue")
vagon(290,350,"blue")
