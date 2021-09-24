import getpass
import os

f = open("countdown_2w.desktop", "x")
s = open("countdown2.sh", "x")

usr = str(getpass.getuser())
f.write("[Desktop Entry]\nVersion=1.0\nName=Countdown 2w\nComment=Simple countdown timer\nExec=python3 /home/"+ usr +"/countdown_timer/countdown2.sh\nIcon=/home/"+ usr +"/countdown_timer/data/countdown.ico\nTerminal=false\nType=Application\nCategories=Application;")
s.write("#!/bin/bash\ncd countdown_timer\npython3 countdown2windows.py")

os.system("chmod +x countdown2.sh")
os.system("mv countdown_2w.desktop ~/Desktop/")
os.system("cd")
os.system("chmod +x ~/Desktop/countdown_2w.desktop")
os.system("gio set ~/Desktop/countdown_2w.desktop metadata::trusted true")
