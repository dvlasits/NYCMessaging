import rsa
from brownie import Sharer, accounts
from scripts.helpful_scripts import get_account, loadObject, Data, getContract
import pickle
from scripts.messagingPart import *




def addObjToTalk(address, message2, privKey):
    print("this even the same??")
    print(address)
    account = accounts.add(privKey)
    sharer = getContract()
    pubkey = sharer.getPubKey(address)
    pubkey = loadObject(pubkey)
    print("this is the pub key")
    print(pubkey)
    message = "CORRECT".encode('utf8')
    encryptedNonce = rsa.encrypt(message, pubkey)
    commFile = str(address)

    print(pubkey)
    print(message2)

    ipnsAddress = createNewIPNS(commFile, message2)

    #ipnsAddress = ipnsAddress.encode("utf8")
    n = 4
    chunks = [ipnsAddress[i:i + n] for i in range(0, len(ipnsAddress), n)]
    ipnsAddress = [rsa.encrypt(i, pubkey) for i in chunks]
    f = open("pubkey", "rb")
    myKey = pickle.load(f)
    f.close()
    myData = Data(encryptedNonce, ipnsAddress, myKey, account.address)

    f = open("temp", "wb")
    pickle.dump(myData, f)
    f.close()

    with open("temp", "rb") as f:
        id = sharer.hashAddress(address)
        sharer.IwantToContact(f.read(), id, {"from": account})



def main(test):
    addObjToTalk(test)