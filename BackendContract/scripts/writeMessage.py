import rsa
from brownie import Sharer
from scripts.helpful_scripts import get_account, loadObject, Data
import pickle
from scripts.messagingPart import *
from scripts.messagingPart import *






def writeMessage(message, address):
    val = updateFile("toSend.txt", message)
    print(val)
    print(updateIPNS(val, address))

def readMessage(address):
    f = open("myConns", "rb")
    myConns = pickle.load(f)
    f.close()
    ipnsName = myConns[address][0]
    print(ipnsName)
    x = getIPNSVal(ipnsName)
    print(x)
    return getIPNSVal(ipnsName)






