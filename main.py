from replit import clear
from art import logo
import os

print(logo)

def get_highest_bidder(bids):
  highest_bid=0
  highest_bidder=''
  for name, bid in bids.items():
    if bid>highest_bid:
      highest_bid=bid
      highest_bidder=name
  print(f"The winner of the aution is {highest_bidder} with bid of {highest_bid}")
bidders_list={}
auction_on=True
while auction_on:
  
  bidders_name=input('Enter your name: ')
  bid=float(input('Enter your bid: '))

  bidders_list[bidders_name]= bid

  more_bidders=input('Are there any more bidders? (y/n)\n').lower()

  if more_bidders=='y':
    clear()
    # if using linux comment line 27 and uncomment the line below
    #os.system('clear')
    # if using windows comment line 27 and uncomment the line below
    #os.system('cls')
  else:
    get_highest_bidder(bidders_list)
    auction_on=False