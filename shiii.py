from tkinter import*
from turtle import color

loop=Tk()
loop.title("Calculator")
loop.geometry("200x260")
#loop.resizable(False,False)
loop.config(background="#efeff5")
#loop.attributes("-alpha",0.9)
loop.iconbitmap('12.ico')
loop.attributes("-topmost",False)
def clicked(num):
    first_num=e1.get()
    e1.delete(0,(END))
    e1.insert(0,str(first_num)+str(num))

def div():
    first_number=e1.get()
    global old_value
    old_value=int(first_number)
    global math
    math="divition"
    e1.delete(0,END)

def minus():
    first_number=e1.get()
    global old_value
    old_value=int(first_number)
    global math
    math="minus"
    e1.delete(0,END)

def add():
    first_number=e1.get()
    global old_value
    old_value=int(first_number)
    global math
    math="addition"
    e1.delete(0,END)

def mul():
    first_number=e1.get()
    global old_value
    old_value=int(first_number)
    global math
    math="multiplication"
    e1.delete(0,END)

def equal():
    if math=="addition":
        new_value=e1.get()
        e1.delete(0,END)
        e1.insert(0,int(old_value)+int(new_value))
    if math=="multiplication":
        new_value=e1.get()
        e1.delete(0,END)
        e1.insert(0,int(old_value)*int(new_value))
    if math=="divition":
        new_value=e1.get()
        e1.delete(0,END)
        e1.insert(0,int(old_value)/int(new_value))
    if math=="minus":
        new_value=e1.get()
        e1.delete(0,END)
        e1.insert(0,int(old_value)-int(new_value))
#myText = StringVar()
#result=Label(loop,text="",textvariable=myText)
#result.place(x=10,y=100)

def clear():
     e1.delete(0,END)

e1=Entry(loop)
e1.place(x=10,y=10)

a = Button(loop,text="7",height=1,width=2,command=lambda:clicked(7))
a.place(x=10,y=60)
b = Button(loop,text="8",height=1,width=2,command=lambda:clicked(8))
b.place(x=40,y=60)
c = Button(loop,text="9",height=1,width=2,command=lambda:clicked(9))
c.place(x=70,y=60)
c = Button(loop,text="x",height=1,width=2,command=mul)
c.place(x=120,y=60)

l = Button(loop,text="4",height=1,width=2,command=lambda:clicked(4))
l.place(x=10,y=100)
m = Button(loop,text="5",height=1,width=2,command=lambda:clicked(5))
m.place(x=40,y=100)
g = Button(loop,text="6",height=1,width=2,command=lambda:clicked(6))
g.place(x=70,y=100)
n = Button(loop,text="+",height=1,width=2,command=add)
n.place(x=120,y=100)


s = Button(loop,text="1",height=1,width=2,command=lambda:clicked(1))
s.place(x=10,y=140,)
e = Button(loop,text="2",height=1,width=2,command=lambda:clicked(2))
e.place(x=40,y=140)
g = Button(loop,text="3",height=1,width=2,command=lambda:clicked(3))
g.place(x=70,y=140)
e = Button(loop,text="_",height=1,width=2,command=minus)
e.place(x=120,y=140)

f= Button(loop,text="/",width=2,command=div)
f.place(x=10,y=180)
v=Button(loop,text="0",height=1,width=2,command=lambda:clicked(0))
v.place(x=40,y=180)
z=Button(loop,text=".",height=1,width=2,command=lambda:clicked("."))
z.place(x=70,y=180)
l=Button(loop,text="=",height=1,width=2,bg='blue',command=equal)
l.place(x=120,y=180)
p=Button(loop,text="clr",command=clear)
p.place(x=160,y=60)
loop.mainloop()