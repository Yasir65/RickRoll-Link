from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def rickroll():
    os.system("sh addnewcount.sh")
    print(f"[{datetime.now()}] [SERVER] Someone Got Rick Rolled!")
    print(f"[{datetime.now()}] [STATUS] You Have Rick Rolled: " + open("rickrollcount.txt", "r").read() + "Times.")
    return render_template("rickroll.html")

@app.route("/count")
def count():
    return render_template("count.html", count=open("rickrollcount.txt", "r").read())

@app.route("/javascript/script/js/script")
def js():
    return open("js.js").read()

@app.errorhandler(404)
def not_found(error):
    os.system("sh addnewcount.sh")
    print(f"[{datetime.now()}] [SERVER] Someone Visited {request.path} 404...")
    print(f"[{datetime.now()}] [SERVER] Redirecting To Rick Roll...")
    print(f"[{datetime.now()}] [SERVER] Someone Got Rick Rolled!")
    print(f"[{datetime.now()}] [STATUS] You Have Rick Rolled: " + open("rickrollcount.txt", "r").read() + "Times.")
    return render_template("rickroll.html")