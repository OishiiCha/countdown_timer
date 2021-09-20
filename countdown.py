from tkinter import *
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    clock_text.config(text = string)
    clock_text.after(1000, time)


def countdown(count):
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
height = 600
width = 600

root = Tk()
root.title("Countdown")
root.resizable(width=False, height=False)
root.configure(bg='black')
root.geometry(str(width) + "x" + str(height))

timer_text = Label(root, font=("Arial", 150), bg="black", fg="white", justify="center")
timer_text.place(x=str(width/2), y=str((height/10)*2), anchor="center")

clock_text = Label(root, font = ('calibri', 40, 'bold'), bg = 'black', fg = 'white')
clock_text.place(x=str(width/2), y=str((height/10)*4), anchor="center")

btn5 = Button(root, text="5", bg="grey", fg="white", font = ('calibri', 40, 'bold'), command=lambda:[countdown(300)])
btn5.place(x=str(width/2), y=str((height/10)*6), anchor="center")

btn10 = Button(root, text="10", bg="grey", fg="white", font = ('calibri', 40, 'bold'), command=lambda:[countdown(600)])
btn10.place(x=str(width/2), y=str((height/10)*8), anchor="center")


time()
root.mainloop()