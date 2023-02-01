from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

counter = nr_letters + nr_symbols + nr_numbers
final_password = ''
index = 0;

while nr_letters != 0:
  index = randint(0, len(letters)-1)
  final_password+=letters[index]
  nr_letters -=1

while nr_symbols !=0:
  index = randint(0, len(symbols)-1)
  final_password+=symbols[index]
  nr_symbols-=1

while nr_numbers !=0:
  index = randint(0, len(numbers)-1)
  final_password+=numbers[index]
  nr_numbers-=1

print(final_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

reshuffled_password = ''

while counter !=0:
  index = randint(0, len(final_password)-1)
  reshuffled_password+=final_password[index]
  final_password = final_password[:index] + final_password[index+1:]
  counter-=1

print(f'Your password is {reshuffled_password}')  