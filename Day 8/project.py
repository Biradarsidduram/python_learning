from caeser_art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

def encrypt(text, shift):
  encoded_text = ''
  for character in text:
    if character in alphabet:
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