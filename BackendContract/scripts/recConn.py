import rsa
from brownie import Sharer, accounts
from scripts.helpful_scripts import get_account, loadObject, Data, getObj, getContract
import pickle
from scripts.messagingPart import *
from pathlib import Path


def recConnec(privKey):
    account = accounts.add(privKey)
    sharer = getContract()
    byteArr = sharer.getDataBasic({"from": account})
    privKey = getObj("privkey")
    print(privKey)
    print(len(byteArr))
    for item in byteArr:
        print("did a loop")
        with open("temp", "wb") as f:
            f.write(item)
        f = open("temp", "rb")
        data = pickle.load(f)
        f.close()
        try:
            data.encryptedNonce = rsa.decrypt(data.encryptedNonce, privKey)
        except rsa.DecryptionError:
            continue
        if data.encryptedNonce == b"CORRECT":
            print
            data.encryptedLink = "".join([str(rsa.decrypt(x,privKey))[2:-1] for x in data.encryptedLink])
            path = Path("myConns")
            if not path.is_file():
                f = open("myConns", "wb")
                pickle.dump(dict(), f)
                f.close()
            f = open("myConns", "rb")
            conns = pickle.load(f)
            f.close()
            conns[data.address] = (data.encryptedLink, data.key)
            print(conns)
            f = open("myConns", "wb")
            pickle.dump(conns, f)
            f.close()




def main():
    recConnec()