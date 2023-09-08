from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task

# for simplicity to get the app running
# create basic app route using the root-level directory of /
# this will be used to target a function called home


@app.route("/")
def home():
    return render_template("base.html")
