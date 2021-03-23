# This is a password generator done as part of the "100 Days of Code - The Complete Pyton Pro Bootcamp for 2021" course by Dr. Angela Yu.
# When writing code as part of courses I am taking, I only upload those excercises/projects I can fully understand and finish without checking the solutions.
# Martin Ignacio Lupa - 11/03/2021.

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the easy PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

for letter in range(1, nr_letters + 1):
  random_letter = random.choice(letters)
  password = password + random_letter

for number in range(1, nr_numbers + 1):
  random_number = random.choice(numbers)
  password = password + random_number

for symbol in range(1, nr_symbols + 1):
  random_symbol = random.choice(symbols)
  password = password + random_symbol

print(f"Your password is: {password}.")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

print("Welcome to the hard PyPassword Generator!")


