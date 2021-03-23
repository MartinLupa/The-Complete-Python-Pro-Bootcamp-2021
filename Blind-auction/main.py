# This is a blind auction program done as part of the "100 Days of Code - The Complete Pyton Pro Bootcamp for 2021" course by Dr. Angela Yu.
# When writing code as part of courses I am taking, I only upload those excercises/projects I can fully understand and finish without checking the solutions.
# Martin Ignacio Lupa - 16/03/2021.

from replit import clear
import art

print(art.logo)
print("Welcome to the secret bid auction system.")

all_bids = {}

bidding_finished = False

def find_highest_bidder(bidding_max):
  winner = ""
  highest_bid = 0
  for bidder in bidding_max:
    bid_amount = bidding_max[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of $ {highest_bid}.")
  print(bid_amount)

while not bidding_finished:
  name = input("What is your name? ")
  bid = int(input("Please place a bid: $ "))
  all_bids[name] = bid
  continue_bids = input("Are there other bidders? 'yes' or 'no'.")
  if continue_bids == "no":
    bidding_finished = True
    find_highest_bidder(all_bids)
  elif continue_bids == "yes":
    clear()









  

