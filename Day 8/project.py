from caeser_art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
  encoded_text = ''
  for character in text:
    if character in alphabet:
      if shift > len(alphabet) -1:
        index = alphabet.index(character) + shift % len(alphabet)
      else:
        index = alphabet.index(character) + shift
      if index > len(alphabet)-1:
        index = index - len(alphabet) + 1
      encoded_text += alphabet[index]
    else:
      encoded_text += character
  print(f"Here's the encoded result: {encoded_text}")

def decrypt(text, shift):
  decoded_text = ''
  for character in text:
    if character in alphabet:
      if shift > len(alphabet) - 1:
        index = alphabet.index(character) - shift % len(alphabet)
      else: 
        index = alphabet.index(character) - shift
      if index < 0:
        index = len(alphabet) -1 + index
      decoded_text += alphabet[index]  
    else:
      decoded_text += character
  print(f"Here's the decoded result: {decoded_text}")    

go_again = 'yes'
while go_again == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction == 'encode':
    encrypt(text, shift)
  else:
    decrypt(text, shift)
  go_again = input("Type 'yes' if you want to go again. Otherwise type 'no' \n").lower()