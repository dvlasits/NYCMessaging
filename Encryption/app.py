from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return open('index.html').read()

@app.route("/call_python", methods = ['POST'])
def call_python():
    print(request.data)

    return "Response from python"