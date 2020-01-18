import tkinter
import random
from random import randrange, randint

X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()


x=0
y=0

kreslit = False
color = "black"
width = 1

def nakresli_plochu():
    canvas.create_rectangle(0,0,800,800, fill = "white")
    
    canvas.create_rectangle(740,540,780,580, fill="black")
    canvas.create_rectangle(700,540,740,580, fill="red")
    canvas.create_rectangle(660,540,700,580, fill="blue")
    canvas.create_rectangle(620,540,660,580, fill="green")

    canvas.create_rectangle(60,540,100,580)
    canvas.create_text(80,560,font=("Arial",12), text="1")
    canvas.create_rectangle(100,540,140,580)
    canvas.create_text(120,560,font=("Arial",12), text="2")
    canvas.create_rectangle(140,540,180,580)
    canvas.create_text(160,560,font=("Arial",12), text="3")


    canvas.create_rectangle(730,20,770,60)
    canvas.create_text(750,40,font=("Arial",12), text="delete")

def klik(event):
    global kreslit, x, y, color, width
    kreslit = True
    x, y = event.x, event.y
    if(x>740 and x<780 and y>540 and y<580):
        color = "black"
    if(x>700 and x<740 and y>540 and y<580):
        color = "red"
    if(x>660 and x<700 and y>540 and y<580):
        color = "blue"
    if(x>620 and x<660 and y>540 and y<580):
        color = "green"

    if(x>60 and x<100 and y>540 and y<580):
        width = 1
    if(x>100 and x<140 and y>540 and y<580):
        width = 5
    if(x>140 and x<180 and y>540 and y<580):
        width = 25
    if(x>730 and x<770 and y>20 and y<60):
        canvas.delete('all')
        nakresli_plochu()
    
    


def kresli(event):        
    global color, width
    if kreslit:
        global x,y
        canvas.create_line(x,y,event.x,event.y, fill = color, width = width)    
        x,y= event.x, event.y



def prestat(event):
    global kreslit, color, width
    kreslit = False
    canvas.create_line(x,y,event.x,event.y, fill = color, width = width)


nakresli_plochu()
canvas.bind("<ButtonPress>",klik)
canvas.bind("<Motion>",kresli)
canvas.bind("<ButtonRelease>",prestat)




