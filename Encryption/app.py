from flask import Flask, render_template
import os;

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/setup")
def setup():
  private_key = "0x952b1d76efd035559bedd3f748d8ef737fc87fdc7efc66285b3fc4770910008f"
  os.system(f"cd ../BackendContract && brownie run setup setup {private_key} --network rinkeby")

  return "Response from python"