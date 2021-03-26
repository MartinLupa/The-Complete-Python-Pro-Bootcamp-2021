# This is a Guessing the Number Game done as part of the "100 Days of Code - The Complete Pyton Pro Bootcamp for 2021" course by Dr. Angela Yu.
#This is a VERSION 2 of the Guessing the Number Game, which includes level of difficulty. Use of Global and Local scope.
# Martin Ignacio Lupa - 26/03/2021.

#Game objectives:
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

logo = """

   _____ _    _ ______  _____ _____ _____ _   _  _____  
  / ____| |  | |  ____|/ ____/ ____|_   _| \ | |/ ____| 
 | |  __| |  | | |__  | (___| (___   | | |  \| | |  __  
 | | |_ | |  | |  __|  \___ \\___ \  | | | . ` | | |_ | 
 | |__| | |__| | |____ ____) |___) |_| |_| |\  | |__| | 
  _______\____/_____________/_____/|_____|_| \_|\_____| 
 |__   __| |  | |  ____|                                
    | |  | |__| | |__                                   
    | |  |  __  |  __|                                  
    | |  | |  | | |____                                 
  _ |__ _|_| _|___________  ______ _____                
 | \ | | |  | |  \/  |  _ \|  ____|  __ \               
 |  \| | |  | | \  / | |_) | |__  | |__) |              
 | . ` | |  | | |\/| |  _ <|  __| |  _  /               
 | |\  | |__| | |  | | |_) | |____| | \ \               
 |______\____/|_| ___|____________|_|  \_\              
  / ____|   /\   |  \/  |  ____|                        
 | |  __   /  \  | \  / | |__                           
 | | |_ | / /\ \ | |\/| |  __|                          
 | |__| |/ ____ \| |  | | |____                         
  \_____/_/    \_\_|  |_|______|                        
                                     
"""

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

difficulty = input("Please choose a difficulty level. Type 'hard' or 'easy': ")

random_number = random.randint(0, 100)


if difficulty == "easy":
  attempts_easy = 10
  for guess in range(0, attempts_easy):
    print(f"You have {attempts_easy} attempts left.")
    guess = int(input("Make a guess: "))
    attempts_easy = attempts_easy - 1
    if guess == random_number:
      print(f"You win! {guess} is the number I was thinking.")
    elif guess > random_number:
      print(f"That is too high. Try a lower number.You have {attempts_easy} attempts left.")
    else:
      print(f"That is too low. Try a higher number.You have {attempts_easy} attempts left.")
  if attempts_easy == 0:
    print("You ran out of attempts. You lose.")


elif difficulty == "hard":
  attempts_hard = 5
  for guess in range(0, attempts_hard):
    print(f"You have {attempts_hard} attempts left.")
    guess = int(input("Make a guess: "))
    attempts_hard = attempts_hard - 1
    if guess == random_number:
      print(f"You win! {guess} is the number I was thinking.")
    elif guess > random_number:
      print(f"That is too high. Try a lower number.You have {attempts_hard} attempts left.")
    else:
      print(f"That is too low. Try a higher number.You have {attempts_hard} attempts left.")
  if attempts_hard == 0:
    print("You ran out of attempts. You lose.")







