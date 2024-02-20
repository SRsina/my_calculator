import clear
from art import logo

def add(n1, n2):
  '''
  This function adds two numbers
  '''
  return n1 + n2

def subtract(n1, n2):
  '''
  This function subtracts two numbers
  '''
  return n1 - n2

def multiply(n1, n2):
  '''
  This function multiply two numbers
  '''
  return n1 * n2

def devide(n1, n2):
  '''
  This function devide two numbers
  '''
  if n2 == 0:
    print("Can't devide by zero")
    return 
  return n1/n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": devide}


def calculator():
  print(logo)
  start = True
  n1 = float(input("What is the first number?: "))
  for key in operations:
    print(key)
  while start:
    operation_symbol = input("Pick an operation from the line above: ")
    n2 = float(input("What is the next number?: "))
    function = operations[operation_symbol]
    result = function(n1, n2)
    print(f"The result of {n1} {operation_symbol} {n2} is = {result}")
    if input(f"Do you want to continue with {result} ? 'y' or for new calculation enter 'n'").lower() == 'n':
      start = False
      clear()
      calculator()
    else:
      n1 = result


calculator()