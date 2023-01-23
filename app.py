from flask import Flask, render_template
import random

app = Flask(__name__, static_folder='static')


@app.route("/")
def index():
    # generates a random number between 10 and 20
    num_cells = random.randint(10, 20)
    return render_template("index.html", num_cells=num_cells)


@app.route("/generate_table")
def generate_table():
    num_cells = random.randint(10, 20)
    table_html = render_template("table.html", num_cells=num_cells)
    return table_html
