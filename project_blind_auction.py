from replit import clear
import art


print(art.logo)
bids = {}
biddig_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"lucas": 123, "dongwoon": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bit of ${highest_bid}")
    
  

while not biddig_finished:
  name = input("What is your name? ")
  price =  int(input("What is your bid? $ "))
  bids[name] = price
  ask_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if ask_continue == "no":
    biddig_finished = True
    find_highest_bidder(bids)
  elif ask_continue == "yes":
    clear()
