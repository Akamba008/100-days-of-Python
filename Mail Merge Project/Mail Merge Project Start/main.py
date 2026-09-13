name_list = []
with open("Input/Names/invited_names.txt") as name_file:
    for line in name_file:
        name = line.rstrip()
        name_list.append(name)

with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:
    invitation_letter = letter_file.read()

text_to_find = "[name]"
count = 0
for name in name_list:
    demo_letter = invitation_letter.replace(text_to_find, name)
    count += 1
    with open(f"Output/ReadyToSend/{name}'s invite.txt", mode="w") as letter_file:
        letter_file.write(demo_letter)

