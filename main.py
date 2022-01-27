from os import system
from time import sleep

open("rickrollcount.txt", "w").write("0 ")
system("gunicorn --bind 0.0.0.0:8000 NiceRickRoll:app &")
print(open("info.txt", "r").read())

while True:
    sleep(60)
    print("[STATUS] You Have Rick Rolled: " + open("rickrollcount.txt", "r").read() + "Times.")