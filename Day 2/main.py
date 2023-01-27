# Day 2 section includes Data Types, Numbers, Operations, Type conversion, f-strings
# Primitive Data types Int, Float, Boolean, Strings

# string dataype

print(len("hello"))

# string concatentation
print("123" + "345")

# integer is a number data type

print(123 + 345)
print(123_345_567)

# Float data type

print(3.146)
print(3.123)

# Boolean data type

print(True, False)

# Problem takes two digit number from user and add each digits

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
print(int(two_digit_number[0])+ int(two_digit_number[1]))
####################################
#Write your code below this line 
# 

def concat(a,b):
  return str(a) + str(b)

str_name = concat(23,32)


# problem BMI calculator

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

BMI = int(int(weight)/ float(height) ** 2)

print(BMI)

#Write your code below this line 👇

num = int(input("Please enter num "));

value = num % 2

type = ''

if value == 0:
  type = 'Even'
else:
  type = 'Odd'

# f string 

print(f"num {num} is {type}")

# problem life in weeks

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_left = 90

age_int = age_left - int(age)

days = int(age_int * (365))

weeks = int(age_int * 52)

months = age_int * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")