import os

from brownie import Sharer
from scripts.helpful_scripts import get_account
import rsa
from os.path import exists
from pathlib import Path
import pickle

def setup():
    account = get_account()
    sharer = Sharer[-1]
    bool = sharer.checkUser({"from": account})
    if bool:
        return
    (pubkey, privkey) = rsa.newkeys(256, poolsize=8)
    f = open("pubkey", "wb")
    pickle.dump(pubkey, f)
    f.close()
    os.remove("privkey")
    f = open("privkey", "wb")
    f.truncate(0)
    pickle.dump(privkey, f)
    f.close()

    with open("pubkey", "rb") as f:
        sharer.addPublicKey(f.read(), {"from": account})


def main():
    setup()