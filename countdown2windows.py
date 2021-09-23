from tkinter import *
from time import strftime
import sounddevice as sd
import soundfile as sf
import time

# pip install soundfile sounddevice

filename = 'data/bell.wav'
data, fs = sf.read(filename, dtype='float32')

syncfile = 'data/sync.wav'
sdata, sfs = sf.read(syncfile, dtype='float32')

def toggle():
    global bell_trigger
    if btnbell.config('text')[-1] == 'Bell on':
        btnbell.config(text='Bell off', bg="black")
        bell_trigger = False
    else:
        btnbell.config(text='Bell on', bg="orange")
        bell_trigger = True

def sync():
    sd.play(sdata, sfs)
    status = sd.wait()

def bell():
    sd.play(data, fs)
    status = sd.wait()

def timed():
    string = strftime('%H:%M:%S %p')
    clock_text.config(text = string)
    clock_text.after(1000, timed)
    clock_text_r.config(text=string)


global running
running = True

def on_start():
    sync()
    global running
    running = True

def on_stop():
    if bell_trigger == 1:
        toggle()
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
    timer_text_r['text'] = r
    if count > 0:
        root.after(1000, countdown, count-1)
    if count == 0 and bell_trigger == 1:
        bell()

global bell_trigger
bell_trigger = False




# sizes
height = 450
width = 450
textsize = 20

w2height = 400
w2width = 600

row1 = str((height/20)*9)
row2 = str((height/20)*12)
row3 = str((height/20)*15)
row4 = str((height/20)*18)
column1 = str((width/20)*2)
column2 = str((width/20)*6)
column3 = str((width/20)*10)
column4 = str((width/20)*14)
column5 = str((width/20)*18)


# Main window
root = Tk()
root.title("Countdown")
root.resizable(width=False, height=False)
root.configure(bg='SkyBlue4')
root.geometry(str(width) + "x" + str(height))
root.iconbitmap('data/countdown.ico')

# Second window
window2 = Tk()
window2.title("Clock")
window2.resizable(width=False, height=False)
window2.configure(bg='black')
window2.geometry(str(w2width) + "x" + str(w2height))
window2.iconbitmap('data/countdown.ico')


timer_text = Label(window2, font=("Arial", 150, 'bold'), bg="black", fg="white", justify="center")
timer_text.place(x=str(w2width/2), y=str((w2height/20)*8), anchor="center")

clock_text = Label(window2, font = ('calibri', 40, 'bold'), bg = 'black', fg = 'white')
clock_text.place(x=str(w2width/2), y=str((w2height/20)*14), anchor="center")

timer_text_r = Label(root, font=("Arial", 40, 'bold'), bg="SkyBlue4", fg="white", justify="center")
timer_text_r.place(x=str((width/20)*10), y=str((height/10)*2), anchor="center")

clock_text_r = Label(root, font = ('calibri', 20, 'bold'), bg = 'SkyBlue4', fg = 'white')
clock_text_r.place(x=str((width/20)*10), y=str((height/10)*3), anchor="center")

title1 = Label(root, height=1, width=20, text="Countdown Clock", bg="SkyBlue4", fg="white", font = ('calibri', textsize, 'bold'))
title1.place(x=str((width/20)*10), y=str((height/10)*1), anchor="center")

btn3 = Button(root, height=1, width=4, text="3", bg="grey", fg="black", font = ('calibri', textsize, 'bold'), command=lambda:[on_start(), countdown(180), sync()])
btn3.place(x=column1, y=row1, anchor="center")

btn4 = Button(root, height=1, width=4, text="4", bg="grey", fg="black", font = ('calibri', textsize, 'bold'), command=lambda:[on_start(), countdown(240)])
btn4.place(x=column2, y=row1, anchor="center")

btn5 = Button(root, height=1, width=4,  text="5", bg="grey", fg="black", font = ('calibri', textsize, 'bold'), command=lambda:[on_start(), countdown(300)])
btn5.place(x=column1, y=row2, anchor="center")

btn10 = Button(root, height=1, width=4,  text="10", bg="grey", fg="black", font = ('calibri', textsize, 'bold'), command=lambda:[on_start(), countdown(600)])
btn10.place(x=column2, y=row2, anchor="center")

btn15 = Button(root, height=1, width=4,  text="15", bg="grey", fg="black", font = ('calibri', textsize, 'bold'), command=lambda:[on_start(), countdown(900)])
btn15.place(x=column1, y=row3, anchor="center")

btn30 = Button(root, height=1, width=4,  text="30", bg="grey", fg="black", font = ('calibri', textsize, 'bold'), command=lambda:[on_start(), countdown(1800)])
btn30.place(x=column2, y=row3, anchor="center")

btn60 = Button(root, height=1, width=4,  text="60", bg="grey", fg="black", font = ('calibri', textsize, 'bold'), command=lambda:[on_start(), countdown(3600)])
btn60.place(x=column1, y=row4, anchor="center")

btn0 = Button(root, height=1, width=4,  text="Own", bg="grey", fg="black", font = ('calibri', textsize, 'bold'), command=lambda:[on_start(), countdown(int(ent.get())*60)])
btn0.place(x=column3, y=row4, anchor="center")

ent = Entry(root, width=4, justify="center", bg="grey", fg="black", font = ('calibri', textsize, 'bold'))
ent.place(x=column2, y=row4, anchor="center")

btnpb = Button(root, height=1, width=4,  text="Bell", bg="black", fg="white", font = ('calibri', textsize, 'bold'), command=lambda:[bell()])
btnpb.place(x=column5, y=row4, anchor="center")

btnstp = Button(root, height=0, width=6, text="Clear", bg="orange", fg="black", font = ('calibri', 20, 'bold'), command=lambda:[toggle(), on_stop()])
btnstp.place(x=column4, y=row2, anchor="center")

btnbell = Button(root, height=0, width=6, text="Bell off", bg="black", fg="white", font = ('calibri', 20, 'bold'), command=toggle)
btnbell.place(x=column4, y=row1, anchor="center")


countdown(0)
timed()
root.mainloop()