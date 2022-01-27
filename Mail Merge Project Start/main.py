# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
with open("Input/Letters/starting_letter.txt", "r") as letter:
    starting_letter = letter.readlines()  # open and read the file and it will us a list
with open("Input/Names/invited_names.txt") as names:
    invited_names = names.readlines()


def listToString(example):  # Convert the list of starting_letter into a string text
    new_starting_letter = ""
    for ele in example:
        new_starting_letter += ele
    return new_starting_letter


new_string_letter = listToString(starting_letter)

for name in invited_names:  # Get hold of the name in invited_names
    stripped_name = name.strip()  # strip off the space between name and the text
    new_letter = new_string_letter.replace("[name]", stripped_name)  # replace the name in each text
    print(new_letter)
    with open(f"Output/ReadyToSend/letter_{stripped_name}.txt", mode="w") as file:
        # save the letter in the name of the receiver
        file.write(new_letter)

# print(invited_names)

# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp

# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
