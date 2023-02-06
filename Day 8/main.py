# Function Parameters & Ceaser Cipher

# Function which takes input and perform operations on top of that.
# to declare function use def keyword and then function name followed by paranthesis

from math import ceil

def greet():
  print("Hello")
  print("How do you do?")
  print("Isn't the weather nice today!")
  

def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you {name}")

greet()
greet_with_name("Siddu Ram")

# Positional vs Keyword Arguments

# Function with multiple inputs or more than one input

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"You are currently living in {location}")

greet_with("siddu", "Hyderabad")

# positional arguments
greet_with(name="Angela", location="London")
greet_with(location="Hyderabad", name="siddu")


# Write a program to calculate no of cans needed to paint wall of width w and height h where each takes a cover of 5 square meters.

#Write your code below this line 👇


def paint_calc(width, height, cover = 5):
  cans = ceil(width * height / cover)
  print(f"You'll need {cans} cans of paint.")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# parameters and keyword arguments spells has to match.


# A function which takes integer and check whether it's a prime number or not
#Write your code below this line 👇


def prime_checker(number):
  range_number = 10
  if number < 10:
    range_number = number

  for check in range(2, range_number):
    if number % check == 0:
      print("It's not a prime number.")
      return
print("It's a prime number.")
    
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

#