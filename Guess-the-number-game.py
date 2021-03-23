# This is a guess the number game done as part of the "Automate the boring stuff" course by Al Sweigart.
# When writing code as part of courses I am taking, I only upload those excercises/projects I can fully...
# understand and finish without checking the solutions.
# Martin Ignacio Lupa - 12/03/2021.

import random

name = input("Hello, what is your name?\n")
print(f"Hi {name}, I just thought of a number between 1 and 10.")

random_num = random.randint(1, 11)

# This function loops/repeats for as many times as defined inside the range.
for guesses_taken in range(1, 7):
    guess = int(input("Take a guess..."))
    if random_num < guess:
        print("That is too high, try a lower number. Choose another.")
    elif random_num > guess:
        print("That is too low, try a higher number. Choose another.")
    else:
        break

if random_num == guess:
    print("You won, that was the number I was thinking!")
else:
    print(f"The number I was thinking was {random_num}.")