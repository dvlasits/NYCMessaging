import os
from random import random
import subprocess

def getIPNSVal(key):
    url = "https://gateway.ipfs.io/ipns/" + key
    result = subprocess.run(["curl", url], stdout=subprocess.PIPE)
    val = result.stdout
    return val

def getFileVal(val):
    print(val)
    result = subprocess.run(["ipfs", "cat", val], stdout=subprocess.PIPE)
    return result.stdout

def updateFile(name, writing):
    with open(name, "w") as f:
        f.write(writing)
    result = subprocess.run(["ipfs", "add", name], stdout=subprocess.PIPE)
    val = (result.stdout.split()[1])
    return val

def updateIPNS(hashFile, name):
    result = subprocess.run(["ipfs", "name", "publish","--key=" + name , "/ipfs/" + str(hashFile)[2:-1]], stdout=subprocess.PIPE)

    x = result.stdout.split()
    print(x)
    x = x[2]
    ipnsAddress = str(x)[2:-2]
    return (ipnsAddress,x)


def createNewIPNS(nof, message):
    val = updateFile(nof, message)
    print(val)
    return val
    result = subprocess.run(["ipfs", "key", "gen", nof], stdout=subprocess.PIPE)

    (ipnsAddress, real) = updateIPNS(val,nof)

    return (ipnsAddress, real)

    """val = updateFile(nof, "lol")

    updateIPNS(val, nof)
    #result = subprocess.run(["ipfs", "name", "publish", "/ipfs/" + str(val)[2:-1]], stdout=subprocess.PIPE)
    print(getIPNSVal(ipnsAddress))"""

def main():
    createNewIPNS()