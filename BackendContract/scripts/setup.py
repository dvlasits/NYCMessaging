import os

from brownie import Sharer, accounts
from scripts.helpful_scripts import get_account, getContract
import rsa
from os.path import exists
from pathlib import Path
import pickle
from time import sleep

def setup(privKey):
    account = accounts.add(privKey)
    sharer = getContract()
    bool = sharer.checkUser({"from": account})
    (pubkey, privkey) = rsa.newkeys(256, poolsize=8)
    f = open("pubkey", "wb")
    pickle.dump(pubkey, f)
    f.close()
    
    f = open("privkey", "wb")
    pickle.dump(privkey, f)
    f.close()

    sleep(0.1)

    with open("pubkey", "rb") as f:
        sharer.addPublicKey(f.read(), {"from": account})


def main():
    setup()