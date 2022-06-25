from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/call_python", methods = ['POST'])
def call_python():
    print(request.data)

    return "Response from python"