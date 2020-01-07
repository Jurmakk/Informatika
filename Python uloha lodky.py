from tkinter import *
import random

master= Tk()
canvas_width = 800
canvas_height = 600

w = Canvas(master, width = canvas_width, height = canvas_height)#
w.pack()

def pozadie():
    w.create_rectangle(0,300,800,600, fill="darkblue")
    w.create_rectangle(0,0,800,300, fill="white")

def mesiac():
    y = random.randint(10,210)
    w.create_oval(500,y,580,y+80, fill="yellow", outline = "yellow")
    w.create_oval(520,y, 600, y+80, fill="white", outline = "white")
    premenna = 300+300-y-80
    w.create_oval(500,premenna,580,premenna+80, fill="yellow", outline = "yellow")
    w.create_oval(520,premenna, 600, premenna+80, fill="darkblue", outline = "darkblue")

    
pozadie()
mesiac()

def flajka(x,y, farba):
    w.create_oval(x,y+20,x+150,y-20,fill="brown")
    w.create_rectangle(x,y+20,x+150,y, fill="darkblue", outline="darkblue")
    w.create_line(x+75,y-20,x+75,y-150)
    w.create_rectangle(x+75,y-150,x+200,y-250, fill=farba)


flajka(10,300, "green")
flajka(540,300,"red")


def mesiac2(x,y,farba1,farba2):
    w.create_oval(x,y,x+80,y+60, fill=farba1, outline = farba1)
    w.create_oval(x+20,y,x+100,y+60, fill=farba2, outline = farba2)

def doublemesiac(x,y,farba1,farba2,velkost):
    w.create_oval(x,y,x+60+velkost,y+40+velkost, fill=farba1, outline = farba1)
    w.create_oval(x+20,y,x+61+velkost,y+40+velkost, fill=farba2, outline = farba2)
    w.create_oval(x-60,y,x+velkost,y+40+velkost, fill=farba1, outline = farba1)
    w.create_oval(x-61,y,x-20+velkost,y+40+velkost, fill=farba2, outline = farba2)

doublemesiac(678,70,"lightblue","red",0)
mesiac2(100,70,"red","green")

def lodka(x,y,velkost):
    w.create_polygon(x,y,x+180+velkost,y,x+130+velkost,y+40+velkost/2,x+50,y+40+velkost/2, fill="darkgoldenrod", outline="black")
    w.create_rectangle(x+85,y,x+95+velkost/2,y-120-velkost,fill="brown", outline="brown")
    w.create_polygon(x+90,y-15,x+125+velkost,y-20,x+90,y-120-velkost, fill="white", outline="black")

for i in range (1,4):
    lodka(300,270,0)
    lodka(170,330,20)
    lodka(40,390,40)

doublemesiac(395,275,"lightblue","darkgoldenrod",-15)
doublemesiac(280,340,"lightblue","darkgoldenrod",-10)
doublemesiac(150,400,"lightblue","darkgoldenrod",0)

x1 = 300
x2 = 395
x3 = 170
x4 = 280
x5 = 40
x6 = 150
def nakresli_lodky():
    global x1, x2
    if x2<2000 and x1>2000:
        return
    global x3, x4
    if x3<2000 and x4>2000:
        return
    global x5, x6
    if x5<2000 and x6>2000:
        return
    w.delete('all')

    pozadie()
    flajka(540,300,"red")
    x1+=1
    x2+=1
    x3+=2
    x4+=2
    x5+=3
    x6+=3

    lodka(x1,270,0)
    doublemesiac(x2,275,"lightblue","darkgoldenrod",-15)

    lodka(x3,330,20)
    doublemesiac(x4,340,"lightblue","darkgoldenrod",-10)

    lodka(x5,390,40)
    doublemesiac(x6,400,"lightblue","darkgoldenrod",0)

    
    mesiac2(500, 80,"yellow" ,"white")
    mesiac2(500, 500, "yellow","darkblue")
   
    flajka(10,300, "green")
    doublemesiac(678,70,"lightblue","red",0)
    mesiac2(100,70,"red","green")

    w.after(10,nakresli_lodky)
    
    

nakresli_lodky()
w.mainloop()

