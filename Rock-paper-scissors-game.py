# This is a Rock, Paper, Scissors game done as part of the "100 Days of Code - The Complete Pyton Pro Bootcamp for 2021" course by Dr. Angela Yu.
# When writing code as part of courses I am taking, I only upload those excercises/projects I can fully understand and finish without checking the solutions.
# Martin Ignacio Lupa - 11/03/2021.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
print(game_images[user_choice])

print("Computer chose:")
computer_choice = random.randint(0, 2)
print(game_images[computer_choice])

#ROCK, PAPER, SCISSORS RULES:

if user_choice == computer_choice:
  print("Draw.")
if user_choice == 0 and computer_choice == 1:
  print("You lose.")
if user_choice == 0 and computer_choice == 2:
  print("You win.")
if user_choice == 1 and computer_choice == 0:
  print("You win.")
if user_choice == 1 and computer_choice == 2:
  print("You lose.")
if user_choice == 2 and computer_choice == 0:
  print("You lose.")
if user_choice == 2 and computer_choice == 1:
  print("You win.")
else:
  print("You chose an invalid input. You lose!.")

