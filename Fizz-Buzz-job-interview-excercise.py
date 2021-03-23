# This is a FizzBuzz game done as part of the "100 Days of Code - The Complete Pyton Pro Bootcamp for 2021" course by Dr. Angela Yu.
# When writing code as part of courses I am taking, I only upload those excercises/projects I can fully understand and finish without checking the solutions.
# Martin Ignacio Lupa - 11/03/2021.

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
