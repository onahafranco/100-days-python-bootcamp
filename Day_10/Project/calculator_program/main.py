from replit import clear
#the clear() can only be found in replit module

from art import logo
def add(n1, n2):
  """a function that adds to numbers when called"""
  return n1 + n2
def subtract(n1, n2):
  """a function that subtracts two numbers when called"""
  return n1 - n2
def multiply(n1, n2):
  """a function that multiplies two numbers when called"""
  return n1 * n2
def divide(n1, n2):
  """a function that divides two numbers when called"""
  return n1 / n2

#creating an empty dictionary 
operators = {}

#assigning keys and values to the dictionary
operators["+"] = add
operators["-"] = subtract
operators["*"] = multiply
operators["/"] = divide
print(logo)

#defining the calculator function for recursive purposes
def calculator():
  num1 = float(input("whats the first number: "))
  
  #setting up condition for the while loop
  continue_calc = True
  while continue_calc:
    for symbol in operators:
      print(symbol)
    operator_choice = input("pick up an operation from the line above: ")
    
    num2 = float(input("whats the next number: "))
    
    calculation_function = operators[operator_choice]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operator_choice} {num2} = {answer}")
    choice = input(f"type y if you with to continue calculating with {answer} or type n to exit program: ")
    if choice == "y":
      num1 = answer
      clear()
    else:
      continue_calc = False
      clear()
      calculator()
  
calculator()

