from brownie import Sharer
from scripts.helpful_scripts import get_account


def main():
    account = get_account()
    print(account)