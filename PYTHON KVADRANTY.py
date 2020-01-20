import tkinter
import random
from random import randrange, randint
X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

x=0
y=0
kreslit = False


def klik(event):
    global kreslit, x, y
    kreslit = True
    x, y = event.x, event.y


def kresli(event):        
    if kreslit:
        global x,y
        r=2
        canvas.create_oval(x-r,y-r,x+r,y+r,fill="red")    
        x,y= event.x, event.y
        a=X_MAX-x
        b=Y_MAX-y
    
        canvas.create_oval(a-r,b-r,a+r,b+r,fill="green")
        canvas.create_oval(x-r,b-r,x+r,b+r,fill="blue")
        canvas.create_oval(a-r,y-r,a+r,y+r,fill="yellow")
        
        
def prestat(event):
    global kreslit
    kreslit = False
    canvas.create_oval(x,y,event.x,event.y)


canvas.bind("<ButtonPress>",klik)
canvas.bind("<Motion>",kresli)
canvas.bind("<ButtonRelease>",prestat)
