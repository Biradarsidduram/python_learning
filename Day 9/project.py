# An auction program 
from art import logo

print(logo)

bidders_dict = []


def get_user_name_bid():
  name= input("What is your name?: ").lower()
  amount = int(input("What is your bid?: $"))
  return {
    'name': name,
    'amount': amount
  }

def get_highest_bidder():
  amount = 0
  name = ''
  for bidder in bidders_dict:
    if amount < bidder['amount']:
      amount = bidder['amount']
      name = bidder['name']
  return { 'name' : name, 'amount': amount }

bidders_dict.append(get_user_name_bid())

is_no_bidders = ''

while True:
  is_no_bidders = input('Are there any other bidders? Type \'yes\' or \'no.\'\n').lower()
  if is_no_bidders == 'no':
    highest_bidder = get_highest_bidder()
    print(f"The winner is {highest_bidder['name']} with a bid of ${highest_bidder['amount']}")
    break
  bidders_dict.append(get_user_name_bid())