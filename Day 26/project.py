# Nato Alphabet Challenge
from pandas import DataFrame, read_csv
from os import system

system('clear')

alpha_file = read_csv('nato_phonetic_alphabet.csv')
nato_names = { row.letter: row.code for index, row in alpha_file.iterrows() }

def generate_phonetic():
  user_name = input("Please enter your name ").upper()
  try:
    phonetic_code_words = [ nato_names[letter] for letter in user_name]
    print(phonetic_code_words)
  except KeyError:
    print("Sorry, only letters in the alphabet please.")  
    generate_phonetic()

generate_phonetic()