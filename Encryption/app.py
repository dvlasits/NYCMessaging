from flask import Flask, render_template
from flask import request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/call_python", methods = ['POST'])
def call_python():
    print(request.data)

    return "Response from python"

@app.route("/call_brownie", methods = ['POST'])
def call_brownie():
    os.system("cd ../BackendContract && brownie run setup --network ganache-local")

    return "Tried to deploy a contract"