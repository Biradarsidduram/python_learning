#  Higher or Lower Game
from art import logo, vs
from game_data import data
from random import choice
from os import system


def get_random_data(game_data, first_random_data = False):
  random_data = choice(game_data)
  if first_random_data and random_data == first_random_data['name']:
    return get_random_data(game_data, first_random_data)
  return random_data


first_random_data = get_random_data(data)
second_random_data = get_random_data(data,first_random_data)
score = 0

def get_person_detail(person_detail):
  return f"{person_detail['name']}, a {person_detail['description']}, from {person_detail['country']}"

def game_comparsion():
  global first_random_data, second_random_data, score
  system('clear')
  print(logo)
  if score:
    print(f"You're right! Current score: {score}.")
  print(f"Compare A: {get_person_detail(first_random_data)}")
  print(vs)
  print(f"Against B: {get_person_detail(second_random_data)} ")
  compare_follower = input("Who has more followers? Type 'A' or 'B': ").lower()
  if  ( compare_follower == 'a' and first_random_data['follower_count'] > second_random_data['follower_count'] ) or ( compare_follower == 'b' and  first_random_data['follower_count'] < second_random_data['follower_count']):
    score+=1
    first_random_data = second_random_data
    second_random_data = get_random_data(data, first_random_data)
    return game_comparsion()
  else:
    print(f"Sorry, that's wrong, Final score: {score}")
    return
  
game_comparsion()