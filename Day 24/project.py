invited_guest_lists = []

with open("Input/Names/invited_names.txt") as guestFile:
  guest_lists =  guestFile.readlines()
  for guest in guest_lists:
    if guest.strip():
      invited_guest_lists.append(guest.strip())


greeting_message = ''

with open("Input/Letters/starting_letter.txt") as letterFile:
  greeting_message = letterFile.read().strip()

for name in invited_guest_lists:
  if name:
    message = greeting_message.replace('[name]', name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", 'w') as inviteFile:
      inviteFile.write(message)  