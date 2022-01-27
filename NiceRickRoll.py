from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def rickroll():
    os.system("sh addnewcount.sh")
    print("[SERVER] Someone Got Rick Rolled!")
    print("[STATUS] You Have Rick Rolled: " + open("rickrollcount.txt", "r").read() + "Times.")
    return render_template("rickroll.html")

@app.route("/count")
def count():
    return render_template("count.html", count=open("rickrollcount.txt", "r").read())

@app.route("/javascript/script/js/script")
def js():
    return open("js.js").read()