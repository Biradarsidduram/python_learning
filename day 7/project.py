# Section Hangman Project

from random import choice
from hangman_words import word_list
from hangman_art import pics, logo

random_word = choice(word_list)
# random_word = 'booooob'
generated_word = '_' *len(random_word)
guess_count = 0
chances = 0

print(logo)

print(random_word)
print(generated_word)

while chances != len(pics):
  guess_character = input("Guess a letter: ").lower( )
  if not bool(guess_character):
    print(pics[chances])
    continue
  if guess_character in random_word:
    guess_count+=1
    index = random_word.index(guess_character)
    if index == generated_word.find(guess_character):
      repitated_index = 0
      while True:
        if repitated_index > index and random_word[repitated_index] == guess_character and generated_word[repitated_index] != guess_character :
          index = repitated_index
          repitated_index = 0
          break   
        if repitated_index == len(random_word)-1:
          print(f"Letter {guess_character} has already been guessed")
          break
        repitated_index+=1
    if index == 0:
      generated_word = guess_character + generated_word[index+1: ]
    else:
      generated_word = generated_word[0:index] + guess_character + generated_word[index+1:]
    print(generated_word)
    print(pics[chances])
  else:
    print(generated_word)
    print(pics[chances])
    chances+=1
  if guess_count == len(random_word) or '_' not in generated_word :
    print("You win")
    break;