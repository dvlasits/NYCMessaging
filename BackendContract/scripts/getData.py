from brownie import Sharer
from scripts.helpful_scripts import get_account


def get_data():
    account = get_account()
    sharer = Sharer[-1]
    allMessages = sharer.getDataBasic({"from": account})


def main():
    get_data()