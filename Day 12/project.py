# Number Guessing Game!
from art import logo
from random import choice
from os import system

def begin_game():
  system('clear')
  random_num = choice(range(1,101))
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  choice_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  attempts = 5
  if choice_level == 'easy':
    attempts += 5

  while attempts:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess_number = int(input("Make a guess: "))
    attempts -=1
    if guess_number == random_num:
      print(f"You got it! The answer was {guess_number}")
      break
    elif attempts == 0:
      print(f"You lost the game!.\nNumber guessed is {guess_number}")
      break
    elif guess_number < random_num:
      print("Too low. \nGuess again.")
    else:
      print("Too high. \nGuess again.")
begin_game()
