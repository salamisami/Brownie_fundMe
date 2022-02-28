from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    print("Getting latest contract..")
    fund_me = FundMe[-1]
    print("Getting account...")
    account = get_account()
    print("getting entrance fee...")
    entrance_fee = fund_me.getEntranceFee()
    print(f"Entry fee is: {entrance_fee}")
    fund_me.fund({"from": account, "value": entrance_fee})
    print("Funded!")

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw{"from": account}
    
def main():
    fund()
