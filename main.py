import platform
from art import logo
import os

print(logo)


def get_highest_bidder(bids):
    highest_bid = 0
    highest_bidder = ''
    for name, bid in bids.items():
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = name
    print(
        f"The winner of the aution is {highest_bidder} with bid of {highest_bid}"
    )


def clear():
    system = platform.system()
    if system == "Linux":
        command = 'clear'
    if system == "Windows":
        command = 'cls'

    os.system(command)


bidders_list = {}
auction_on = True
while auction_on:

    bidders_name = input('Enter your name: ')
    bid = float(input('Enter your bid: '))

    bidders_list[bidders_name] = bid

    more_bidders = input('Are there any more bidders? (y/n)\n').lower()

    if more_bidders == 'y':
        clear()
    else:
        get_highest_bidder(bidders_list)
        auction_on = False
