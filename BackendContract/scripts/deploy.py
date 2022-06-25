from brownie import Sharer, accounts
from scripts.helpful_scripts import get_account


def deploy_sharer(privKey):
    account = accounts.add(privKey)
    sharer = Sharer.deploy({"from": account}, publish_source=True)
    print(f"Contract deployed to {sharer.address}")


def main():
    deploy_sharer()