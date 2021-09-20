from tkinter import *
from time import strftime
import time

def timed():
    string = strftime('%H:%M:%S %p')
    clock_text.config(text = string)
    clock_text.after(1000, timed)

global running
running = True

def on_start():
    global running
    running = True

def on_stop():
    global running
    running = False

def countdown(count):
    if running == False:
        count = 0
    a = divmod(count, 60)
    if len(str(a[0])) == 1:
        m = "0" + str(a[0])
    else:
        m = str(a[0])
    if len(str(a[1])) == 1:
        s = "0" + str(a[1])
    else:
        s = str(a[1])
    r = m + ":" + s
    timer_text['text'] = r
    if count > 0:
        root.after(1000, countdown, count-1)


# sizes
height = 800
width = 600
textsize = 30

root = Tk()
root.title("Countdown")
root.resizable(width=False, height=False)
root.configure(bg='black')
root.geometry(str(width) + "x" + str(height))

timer_text = Label(root, font=("Arial", 150), bg="black", fg="white", justify="center")
timer_text.place(x=str(width/2), y=str((height/10)*2), anchor="center")

clock_text = Label(root, font = ('calibri', 40, 'bold'), bg = 'black', fg = 'white')
clock_text.place(x=str(width/2), y=str((height/10)*4), anchor="center")

btn3 = Button(root, height=0, width=4, text="3", bg="grey", fg="white", font = ('calibri', textsize, 'bold'), command=lambda:[on_start(), countdown(180)])
btn3.place(x=str((width/20)*2), y=str((height/10)*6), anchor="center")

btn4 = Button(root, height=0, width=4, text="4", bg="grey", fg="white", font = ('calibri', textsize, 'bold'), command=lambda:[on_start(), countdown(240)])
btn4.place(x=str((width/20)*6), y=str((height/10)*6), anchor="center")

btn5 = Button(root, height=0, width=4,  text="5", bg="grey", fg="white", font = ('calibri', textsize, 'bold'), command=lambda:[on_start(), countdown(300)])
btn5.place(x=str((width/20)*10), y=str((height/10)*6), anchor="center")

btn10 = Button(root, height=0, width=4,  text="10", bg="grey", fg="white", font = ('calibri', textsize, 'bold'), command=lambda:[on_start(), countdown(600)])
btn10.place(x=str((width/20)*14), y=str((height/10)*6), anchor="center")

btn15 = Button(root, height=0, width=4,  text="15", bg="grey", fg="white", font = ('calibri', textsize, 'bold'), command=lambda:[on_start(), countdown(900)])
btn15.place(x=str((width/20)*18), y=str((height/10)*6), anchor="center")

btn30 = Button(root, height=0, width=4,  text="30", bg="grey", fg="white", font = ('calibri', textsize, 'bold'), command=lambda:[on_start(), countdown(1800)])
btn30.place(x=str((width/5)*2), y=str((height/20)*15), anchor="center")

btn60 = Button(root, height=0, width=4,  text="60", bg="grey", fg="white", font = ('calibri', textsize, 'bold'), command=lambda:[on_start(), countdown(3600)])
btn60.place(x=str((width/5)*3), y=str((height/20)*15), anchor="center")

btnstp = Button(root, height=0, width=10, text="Clear", bg="orange", fg="black", font = ('calibri', 20, 'bold'), command=lambda:[on_stop()])
btnstp.place(x=str(width/2), y=str((height/10)*9), anchor="center")

countdown(0)
timed()
root.mainloop()