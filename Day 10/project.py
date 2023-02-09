#  A calculator program
from art import logo

operations = ['+', '-', '*', '/']
first_number = 0
second_number = 0
operation = ''
new_calculation = 'no'
result = 0

def perform_operation(first_number, second_number, operation):
  if operation == '+':
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")
    return result
  elif operation == '-':
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result}")
    return first_number - second_number
  elif operation == '*':
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")
    return result
  elif operation == '/' :
    result = first_number / second_number
    print(f"{first_number} / {second_number} = {result}")
    return result
def print_operation(operations):
  for operation in operations:
    print(operation)

while True:
  print(logo)  
  if not result:
    first_number = float(input("What's the first number?: "))
  print_operation(operations)
  operation= input("Pick an operation: ")
  second_number = float(input("What's the second number?: "))
  result = perform_operation(first_number,second_number, operation)
  new_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
  if new_calculation == 'n':
    result = 0
  else:
    first_number = result