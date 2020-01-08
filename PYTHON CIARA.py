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
        canvas.create_line(x,y,event.x,event.y)    
        x,y= event.x, event.y

    


    
def prestat(event):
    global kreslit
    kreslit = False
    canvas.create_line(x,y,event.x,event.y)

        



canvas.bind("<ButtonPress>",klik)
canvas.bind("<Motion>",kresli)
canvas.bind("<ButtonRelease>",prestat)



