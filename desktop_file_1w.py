import getpass
import os

f = open("countdown_1w.desktop", "x")

usr = str(getpass.getuser())
f.write("[Desktop Entry]\nVersion=1.0\nName=Countdown 1w\nComment=Simple countdown timer\nExec=python3 /home/"+ usr +"/countdown_timer/countdown.py\nIcon=/home/"+ usr +"/countdown_timer/countdown.ico\nTerminal=false\nType=Application\nCategories=Application;")


os.system("mv countdown_1w.desktop ~/Desktop/")
os.system("cd")
os.system("chmod +x ~/Desktop/countdown_1w.desktop")
os.system("gio set ~/Desktop/countdown_1w.desktop metadata::trusted true")