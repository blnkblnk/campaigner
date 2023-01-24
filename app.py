from flask import Flask, render_template
import random

app = Flask(__name__, static_folder='static')


@app.route("/")
def index():
    return render_template("index.html")

num = 1

@app.route("/generate_table")
def generate_table():
    global num
    num += 1
    num %= 15
    num_cells = random.randint(10, 20)
    num_cells = num
    table_html = render_template("table.html", num_cells=num_cells)
    return table_html
