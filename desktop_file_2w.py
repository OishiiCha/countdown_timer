import getpass
import os

f = open("countdown_2w.desktop", "x")

usr = str(getpass.getuser())
f.write("[Desktop Entry]\nVersion=1.0\nName=Countdown 2w\nComment=Simple countdown timer\nExec=python3 /home/"+ usr +"/countdown_timer/countdown2windows.py\nIcon=/home/"+ usr +"/countdown_timer/data/countdown.ico\nTerminal=false\nType=Application\nCategories=Application;")


os.system("mv countdown_2w.desktop ~/Desktop/")
os.system("cd")
os.system("chmod +x ~/Desktop/countdown_2w.desktop")
os.system("gio set ~/Desktop/countdown_2w.desktop metadata::trusted true")