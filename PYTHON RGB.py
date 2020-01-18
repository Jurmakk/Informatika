import tkinter
import random
from random import randrange

X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()


r,g,b,x=randrange(255),randrange(255),randrange(255),1

while True:
    
    canvas.delete("all")
    color=f"#{r:02x}{g:02x}{b:02x}"
    canvas.create_rectangle(1,1,X_MAX+1,X_MAX+1,fill=color,outline=color)
    
    
    if r==255:
        r=0

    if g==255:
        g=0
        b+=x
        
    b=b+x
    if b==255:
        b=0
        g+=x

    canvas.after(1)
    canvas.update()
