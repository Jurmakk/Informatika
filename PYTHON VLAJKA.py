import tkinter
import random
from random import randrange,randint
X_MAX, Y_MAX = 800,600

canvas=tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()


for i in range (10000):
    x = randrange(X_MAX)
    y = randrange(Y_MAX)
    
    if x < 200 and y < 200:
        farba="blue"
    elif x > 300 and y > 300:
        farba="blue"
    elif x > 300 and y < 200:
        farba="blue"
    elif x < 200 and y > 300:
        farba="blue"
    else:
        farba="yellow"

    canvas.create_rectangle(x-10,y-10,x+10,y+10,fill=farba)
