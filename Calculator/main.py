# This is a calculator program done as part of the "100 Days of Code - The Complete Pyton Pro Bootcamp for 2021" course by Dr. Angela Yu.
# When writing code as part of courses I am taking, I only upload those excercises/projects I can fully understand and finish without checking the solutions.
# Martin Ignacio Lupa - 22/03/2021.

import art
print(art.logo)

#FUNCTIONS DEFINITION:
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+":add, 
  "-":subtract, 
  "*":multiply, 
  "/":divide}

def calculator():
  num1 = int(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)

  should_continue = True

  while should_continue:
    operation_symbol = input("What operation do you want to execute?: ")
    num2 = int(input("What's the next number?: "))
    calculation = operations[operation_symbol]
    answer = calculation(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Do you want to continue calculating with {answer}? 'y' or 'n' to start a new calculation.") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()