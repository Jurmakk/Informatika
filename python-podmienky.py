import tkinter
from random import randrange, randint

X_MAX, Y_MAX=600,600

c=tkinter.Canvas(width=X_MAX, height=Y_MAX, bg="black")
c.pack()

r=50

x,y,= randint(r, X_MAX-r), randint(r, Y_MAX-r)

dy=3
dx=3

def saver(x,y,r, farba):
    c.create_rectangle(x-r,y-r,x+r,y+r,fill=farba)
    c.create_text(x,y, text="DVD", font= "Arial 30", fill= "white")

while True:
    c.delete("all")
    saver(x,y,r,"red")
    y+=dy
    x+=dx

    if y >= Y_MAX-r or y <= r:
        dy*=- 1
    if x <= r or x >= X_MAX-r:
        dx*=- 1

    c.update()
    c.after(1)
    
