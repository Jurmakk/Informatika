import tkinter
c=tkinter.Canvas(width=800, height=600)
c.pack()

x,y=100, 100
for i in range(10):
    c.delete("all")
    idd=c.create_rectangle(x,y,x+50,y+50)
    print(idd)
    x+=30
    c.update
    c.after(1000)
    
