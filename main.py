from replit import clear
from art import logo
should_continue = True
print(logo)
print("Welcome to the secret auction program.")

auction = {}

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  
  print(f"The winner is {winner} with a bid of £{highest_bid}")

while should_continue:
  name = str(input("What is your name?: "))
  bid = int(input("What is your bid?: £"))
  auction[name] = bid
  next_step = input("Are there any other bidders? Type 'yes' or 'no' \n").lower()
  if next_step == "yes":
    clear()
  elif next_step == "no":
    should_continue = False
    clear()
    find_highest_bidder(auction)



  