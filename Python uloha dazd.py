from tkinter import *
import random
from random import randint

master= Tk()
canvas_width = 800
canvas_height = 600

w = Canvas(master, width = canvas_width, height = canvas_height)#
w.pack()


def kvapka(x,y):
    w.create_oval(x-5,y-5,x+5,y+5,fill="lightblue")

def dazd():
    
    for i in range (100,200):
        x=random.randint(0,800)
        y=random.randint(0,800)
        kvapka(x,y)

while True:
    w.delete ("all")
    dazd()
    w.after(50)
    w.update()

    
