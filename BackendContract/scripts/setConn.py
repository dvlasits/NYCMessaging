import rsa
from brownie import Sharer, accounts
from scripts.helpful_scripts import get_account, loadObject, Data, getContract
import pickle
from scripts.messagingPart import *




def addObjToTalk(address, privKey):
    account = accounts.add(privKey)
    sharer = getContract()
    #if not sharer.checkUser(account):
    #    return
    pubkey = sharer.getPubKey(address)
    pubkey = loadObject(pubkey)
    message = "CORRECT".encode('utf8')
    encryptedNonce = rsa.encrypt(message, pubkey)
    commFile = str(address)

    print(pubkey)

    ipnsAddress,_ = createNewIPNS(commFile)

    ipnsAddress = ipnsAddress.encode("utf8")
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

    sharer = Sharer[-1]

    with open("temp", "rb") as f:
        id = sharer.hashAddress(address)
        sharer.IwantToContact(f.read(), id, {"from": account})



def main(test):
    addObjToTalk(test)