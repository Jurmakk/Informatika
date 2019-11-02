from tkinter import *
import random
master= Tk()
canvas_width = 800
canvas_height = 600

w = Canvas(master, width = canvas_width, height = canvas_height)#
w.pack()


def strom(x,y,velkost):
    w.create_rectangle(x+85,y,x+95,y-120,fill="brown", outline="brown")
    w.create_oval(x+90-velkost,y-120-velkost,x+90+velkost,y-120+velkost,fill="green", outline="black")

for i in range(10):
    strom(random.randint(1,800),random.randint(1,600), random.randint(20,50))



def mariska (x,y,pocet_listov):
    for i in range(pocet_listov):
        w.create_line(x,y, x+random.randint(-20,20),y+random.randint(-20,0),width = random.randint(1,3),fill="green")

           
for i in range(20):
    mariska(random.randint(1,800), random.randint(1,600), random.randint(3,10))
