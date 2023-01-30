with open("./Input/Letters/starting_letter.txt") as starting_letter:
    original_letter = starting_letter.read()

with open("./Input/Names/invited_names.txt") as invited_names:
    invite_list = invited_names.readlines()

for invitee in invite_list:
    invitee = invitee.strip()
    message = original_letter.replace("[name]", invitee)
    with open(f"./Output/ReadyToSend/letter_for_{invitee}.txt", mode="w") as invite:
        invite.write(message)
