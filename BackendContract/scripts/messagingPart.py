import os
from random import random
import subprocess

def getIPNSVal(key):
    url = "https://gateway.ipfs.io/ipns/" + key
    result = subprocess.run(["curl", url], stdout=subprocess.PIPE)
    val = result.stdout
    return val

def updateFile(name, writing):
    with open(name, "w") as f:
        f.write(writing)
    result = subprocess.run(["ipfs", "add", name], stdout=subprocess.PIPE)
    val = (result.stdout.split()[1])
    return val

def updateIPNS(hashFile, name):
    result = subprocess.run(["ipfs", "name", "publish","--key=" + name , "/ipfs/" + str(hashFile)[2:-1]], stdout=subprocess.PIPE)

    x = result.stdout.split()[2]
    ipnsAddress = str(x)[2:-2]
    return (ipnsAddress,x)


def createNewIPNS(nof):
    val = updateFile(nof, "test")
    result = subprocess.run(["ipfs", "key", "gen", nof], stdout=subprocess.PIPE)

    (ipnsAddress, real) = updateIPNS(val,nof)

    return (ipnsAddress, real)

    """val = updateFile(nof, "lol")

    updateIPNS(val, nof)
    #result = subprocess.run(["ipfs", "name", "publish", "/ipfs/" + str(val)[2:-1]], stdout=subprocess.PIPE)
    print(getIPNSVal(ipnsAddress))"""

def main():
    createNewIPNS()