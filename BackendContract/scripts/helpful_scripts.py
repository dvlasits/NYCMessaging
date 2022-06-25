from brownie import network, config, accounts, Sharer
import pickle


def getContract():
    sharer = Sharer.at('0xf449BE6D3ebFe65A2d66Ea65aa19842251f88bEf')
    return sharer

class Data:

    def __init__(self, encryptedNonce, encryptedLink, key, address):
        self.address = address
        self.key = key
        self.encryptedNonce = encryptedNonce
        self.encryptedLink = encryptedLink



def getObj(name):
    f = open(name, "rb")
    omj = pickle.load(f)
    f.close()
    return omj




def get_account():
    print("here")
    return accounts[0]
    if network.show_active() == "development" or network.show_active() == "ganache-local":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])



def loadObject(bytes):

    with open("temp", "wb") as f:
        f.write(bytes)
    f = open("temp", "rb")
    obj = pickle.load(f)
    f.close()
    return obj