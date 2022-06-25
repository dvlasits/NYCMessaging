from brownie import network, config, accounts
import pickle


class Data:

    def __init__(self, encryptedNonce, encryptedLink):
        self.encryptedNonce = encryptedNonce
        self.encryptedLink = encryptedLink




def get_account():
    if network.show_active() == "development":
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