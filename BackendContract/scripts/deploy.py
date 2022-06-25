from brownie import Sharer
from scripts.helpful_scripts import get_account


def deploy_sharer():
    account = get_account()
    sharer = Sharer.deploy({"from": account})#, publish_source=True)
    print(f"Contract deployed to {sharer.address}")


def main():
    deploy_fund_me()