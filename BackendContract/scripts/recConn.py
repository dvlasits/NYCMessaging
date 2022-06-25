import rsa
from brownie import Sharer
from scripts.helpful_scripts import get_account, loadObject, Data, getObj
import pickle
from scripts.messagingPart import *
from pathlib import Path



def recConnec():
    account = get_account()
    sharer = Sharer[-1]
    byteArr = sharer.getDataBasic({"from": account})
    privKey = getObj("privkey")
    print(privKey)
    for item in byteArr:
        with open("temp", "wb") as f:
            f.write(item)
        f = open("temp", "rb")
        data = pickle.load(f)
        f.close()
        data.encryptedNonce = rsa.decrypt(data.encryptedNonce, privKey)
        if data.encryptedNonce == b"CORRECT":
            data.encryptedLink = "".join([str(rsa.decrypt(x,privKey))[2:-1] for x in data.encryptedLink])
            path = Path("myConns")
            if not path.is_file():
                f = open("myConns", "wb")
                pickle.dump(dict(), f)
                f.close()
            f = open("myConns", "rb")
            conns = pickle.load(f)
            f.close()
            conns[data.address] = data.encryptedLink




def main():
    recConnec()