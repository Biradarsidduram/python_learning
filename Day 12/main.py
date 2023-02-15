# Section Local vs Global Scope

# Scope is defined as a variable/entity available within the teritory 
# E.g An apple tree wihtin a house yard and owner can eat the apples, others not.

# Here enemies is a global variable and can be available everywhere within a whole main program 

enemies = 1
enemies_strength = '90%'

def increase_enemies():
  # Enemies is a local variable declared a new one
  global enemies, enemies_strength
  enemies_strength = '94%'
  enemies = 2
  print(f"eneemies inside function: {enemies}")

increase_enemies()

print(f"eneemies outside function: {enemies}")

player_health = 10

def drink_potion():
  potion_strength = 2
  print(player_health)

drink_potion()

# Block Scope

if True:
  declare_variable = "Hi there"

print(declare_variable)


# Modify global scope
# use variable global followed by global_variable_name
# global enemies, player_health

# python constants and Global Scope
# There is no constants in python

PI = 3.14159

PI = 'change this value'

print(PI)