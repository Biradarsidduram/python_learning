# Project Rock, Paper, Scissor

from random import randint

user_choose_type = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

random_choose_type = randint(0,2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_images = [rock, paper, scissors]

if user_choose_type > len(game_images)-1 :
  print("Index out of range, you lose")
else:
  print(game_images[user_choose_type])
  print("Computer choose:")
  print(game_images[random_choose_type])
  if user_choose_type == random_choose_type:
    print("It's a draw")
  elif (user_choose_type == 0 and random_choose_type == 2) or (user_choose_type == 1 and random_choose_type == 0) or (user_choose_type == 2 and random_choose_type == 1):
    print("You win!")
  else:
    print("You lose")  
