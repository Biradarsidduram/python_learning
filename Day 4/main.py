#  Section 4 Randomisation, Lists

# Random Module

from random import randint, random

random_int = randint(1,5)

random_float = random_int + random()  

print(f"Random number is {random_int} and random float is f{random_float}")


#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇

number = randint(0,1)

if number == 0:
  print("Heads")
else:
  print("Tails")

# Lists is a way of storing data    

states_of_america = ["Delaware", "Pennsylvania"]

print(states_of_america)

states_of_america.append("New York")

states_of_america = states_of_america[:]

print(states_of_america)

# Problem picks random name from the list who will pay the bill

# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

random_index = randint(0 , len(names)-1)

print(f"{names[random_index]} is going to buy the meal today!")

# Treasure Mapping

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

column = int(position[0])
row = int(position[1])

map[row-1][column-1] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

# Day 4 section completed