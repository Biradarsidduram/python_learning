from art import logo
from random import choice
from os import system

cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]
max_value = 21
player_cards  = []
computer_cards = []


def get_card():
  return choice(cards)

def get_sum_of_cards(player_cards):
  sum =0
  for card in player_cards:
    sum += card
  return sum
  
def fill_card(player_cards):
  card = get_card()
  if card == 1:
    sum = get_sum_of_cards(player_cards)
    if sum + card > 21:
      player_cards.append(1)
    else:
      player_cards.append(card)  
  else:  
    player_cards.append(card)

def print_game_scores():
  player_score = get_sum_of_cards(player_cards)
  computer_score = get_sum_of_cards(computer_cards)
  print(f"    Your cards: {player_cards}, current score: {player_score}")
  print(f"    Computer's card: {computer_cards}, current score: {computer_score}")

def fill_player_card_initial():
  player_cards.clear()
  computer_cards.clear()
  fill_card(player_cards)
  fill_card(player_cards)
  fill_card(computer_cards)
  print_game_scores()

def user_turn():
  get_card_for_user = input("Type 'y' to get another card, type 'n' to pass: ").lower()
  if get_card_for_user == 'y':
    fill_card(player_cards)
  score = get_sum_of_cards(player_cards)
  print_game_scores()
  if score > max_value or get_card_for_user == 'n':
    return score
  return user_turn()

def computer_turn():
  fill_card(computer_cards)
  computer_score = get_sum_of_cards(computer_cards)
  user_score = get_sum_of_cards(player_cards)
  if computer_score < max_value and computer_score < user_score and (computer_score != user_score) :
    return computer_turn()
  else:
    print_game_scores()
    return computer_score

def begin_game():
  continue_gameplay = 'y'
  while True:
    continue_gameplay = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    system('clear')
    if continue_gameplay == 'n':
      return
    print(logo)
    fill_player_card_initial()
    user_score = user_turn()
    if user_score > max_value:
      print("You went over. You lose 😭") 
      continue
    computer_score = computer_turn()
    if user_score == computer_score:
      print("Draw 🙃")
      continue
    elif user_score == max_value:
      print("Win with a Blackjack 😎")
      continue
    elif computer_score == max_value:
      print("You loose with a Blackjack 😭")
      continue
    elif computer_score > max_value:
      print("Opponent went over. You win 😃")
      continue
    elif (user_score <= max_value and user_score > computer_score):
      print("You win 😃")
      continue
    elif (computer_score > user_score and computer_score <= max_value):
      print("You lose 😤")
      continue

begin_game()