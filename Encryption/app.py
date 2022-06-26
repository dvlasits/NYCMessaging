from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)

private_key = "0x952b1d76efd035559bedd3f748d8ef737fc87fdc7efc66285b3fc4770910008f"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/setup")
def setup():
  os.system(f"cd ../BackendContract && brownie run setup setup {private_key} --network rinkeby")

  return "Response from python /setup"

@app.route("/set_con", methods=['GET','POST'])
def set_con():
  data = json.loads(request.data)
  target_address = data['target_address']

  print(target_address)

  os.system(f"cd ../BackendContract && brownie run setConn addObjToTalk {target_address} {private_key} --network rinkeby")

  return "Response from python /set_con"