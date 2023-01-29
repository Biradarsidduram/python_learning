# Section 3 Conditional Statements, Logical Operators, Code Blocks and Scope

# problem check whethere a number is Even or Odd

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Nested if else statement
if number%2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

# If else if statement

print("Welcome to the roller coaster")
height = int( input("What is your height in cm? ") )

if height >=120:
  print("You can ride the rollercoaster")
  age = int( input("What is your age? ") )
  if age<=12:
    print("Please pay $5")
  elif age<=18:
    print("Please pay $7")
  else:
    print("Please pay $12")   
else:
  print("You cannot ride roller coaster")  

#Problem BMI 2.0 Calculator

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

BMI = ( weight/ height **2 )

if BMI<= 18.5:
  print(f'Your BMI is {round(BMI)}, you are underweight.')
elif BMI<= 25:
  print(f"Your BMI is {round(BMI)}, you have a normal weight.")
elif BMI <=30:
  print(f"Your BMI is {round(BMI)}, you are slightly overweight.")
elif BMI <=35:
  print(f"Your BMI is {round(BMI)}, you are obese.")
else:
  print(f"Your BMI is {round(BMI)}, you are clinically obese.")  
#Write your code below this line 👇


# Problem leap year checking

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year% 4 ==0:
  print("Leap year.")
else:
  print("Not leap year.")

# Multiple if statements for the given condition

# Pizza problem 

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

pizza_price = 0

if size == 'S':
    pizza_price+=15
elif size == 'M':
    pizza_price+=20
else:
    pizza_price+=25

if add_pepperoni == 'Y':
    if size == 'S':
        pizza_price+=2
    else:
        pizza_price+=3
if extra_cheese == 'Y':
    pizza_price+=1

print(f"Your final bill is: ${pizza_price}.")

# Logical Operators - and, or, not

# Problem Love calculator

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


name1_lower = name1.lower()
name2_lower = name2.lower()

true_count = 0
love_count = 0

true_count += name1_lower.count('t')
true_count += name1_lower.count('r')
true_count += name1_lower.count('u')
true_count += name1_lower.count('e')
true_count += name2_lower.count('t')
true_count += name2_lower.count('r')
true_count += name2_lower.count('u')
true_count += name2_lower.count('e')

love_count += name1_lower.count('l')
love_count += name1_lower.count('o')
love_count += name1_lower.count('v')
love_count += name1_lower.count('e')
love_count += name2_lower.count('l')
love_count += name2_lower.count('o')
love_count += name2_lower.count('v')
love_count += name2_lower.count('e')

percentage_count = true_count * 10 + love_count

if percentage_count > 90 or percentage_count < 10:
    print(f"Your score is {percentage_count}, you go together like coke and mentos.")
elif percentage_count > 40 and percentage_count < 50:
    print(f"Your score is {percentage_count}, you are alright together.")
else:
    print(f"Your score is {percentage_count}.")       

