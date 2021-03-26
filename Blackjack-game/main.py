# This is a Blackjack game done as part of the "100 Days of Code - The Complete Pyton Pro Bootcamp for 2021" course by Dr. Angela Yu.
# Martin Ignacio Lupa - 26/03/2021.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import art
from replit import clear

def deal_card():
  """Returns a random card from the list 'cards'."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Takes a list of cards and returns the score calculated from the cards."""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "User lost. Opponent has a BlackJack"
  elif user_score == 0: 
    return "You win! You have a BlackJack!"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win!"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lose"

def play():
  print(art.logo)
#USER AND COMPUTER STARTS WITH NO CARDS.
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #FIRST WHILE LOOP, FOR THE USER:
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards : {user_cards} and score is: {user_score}.")
    print(f"Computer's first card is: {computer_cards[0]}.")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card or 'n' to pass.")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  #SECOND WHILE LOOP FOR THE COMPUTER. IT WILL DRAW CARDS AS LONG AS IT HAS A SCORE LESS THAN 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, and your final score is {user_score}.")
  print(f"Opponent's final hand: {computer_cards}, and final score: {computer_score}.")
  print(compare(user_score, computer_score))

while input("Welcome to the CASINO. Do you want to play some BlackJack? Type 'y' or 'n'.") == "y":
  clear()
  play()