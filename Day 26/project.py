# Nato Alphabet Challenge
from pandas import DataFrame, read_csv
from os import system

system('clear')

alpha_file = read_csv('nato_phonetic_alphabet.csv')

user_name = input("Please enter your name ").upper()

nato_names = { row.letter: row.code for index,row in alpha_file.iterrows() }

phonetic_code_words = [ nato_names[letter] for letter in user_name if letter in nato_names ]

print(phonetic_code_words)