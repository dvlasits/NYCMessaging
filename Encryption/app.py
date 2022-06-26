from flask import Flask, render_template, request
import os
import json
import base64

app = Flask(__name__)

private_key = "a65c77708018bc98235d266267fed947f87d87405a36f2573ec2e4f37d49fe9e"#"0x952b1d76efd035559bedd3f748d8ef737fc87fdc7efc66285b3fc4770910008f"
wallet_address = "0x61fF6367537Ab46FccAf06bB9FD05A1b308fb7B6"#"0x66d9fb0Cd2D9103C29fF3a695479875FA422F6A8"

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
  message = data['message']

  message = base64.b64encode(message.encode('utf-8')).decode('ascii')

  print(target_address)
  print(f'message: {message}')

  print(f"cd ../BackendContract && brownie run setConn addObjToTalk {target_address} {message} {private_key} --network rinkeby")
  os.system(f"cd ../BackendContract && brownie run setConn addObjToTalk {target_address} {message} {private_key} --network rinkeby")

  return "Response from python /set_con"


@app.route("/get_con", methods=['POST'])
def get_con():
  data = json.loads(request.data)
  target_address = data['target_address']
  print(target_address)

  os.system(f"cd ../BackendContract && brownie run recConn recConnec {private_key} --network rinkeby")
  os.system(f"cd ../BackendContract && brownie run writeMessage readMessage {target_address} --network rinkeby")

  with open("../BackendContract/textOut.json") as f:
    data = json.load(f)
  
  print(data)

  data['text'] = base64.b64decode(data['text'].encode('ascii')).decode('utf-8')

  return json.dumps(data)

@app.route("/read_message")
def read_message():
  os.system(f"cd ../BackendContract && brownie run writeMessage readMessage {wallet_address} --network rinkeby")

  return "Response from python /read_message"