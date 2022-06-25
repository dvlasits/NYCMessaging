import rsa
from brownie import Sharer
from scripts.helpful_scripts import get_account, loadObject, Data
import pickle
from scripts.messagingPart import *




def addObjToTalk(address):
    account = get_account()
    sharer = Sharer[-1]
    if not sharer.checkUser(account):
        return
    pubkey = sharer.getPubKey(address)
    pubkey = loadObject(pubkey)
    message = "CORRECT".encode('utf8')
    encryptedNonce = rsa.encrypt(message, pubkey)
    commFile = str(address)
    ipnsAddress = createNewIPNS(commFile)
    myData = Data(encryptedNonce, ipnsAddress)
    print(myData)





def main(test):
    addObjToTalk(test)