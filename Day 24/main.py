# file = open("my_file.txt")
# contents = file.read()
# print(contents)

with open("new_file.txt", mode="w") as file:
    file.write("Scratch that!")