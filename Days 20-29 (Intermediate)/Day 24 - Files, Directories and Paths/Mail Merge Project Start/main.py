#  Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Minha solução ##
# nomes = []
# with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as names:
#     for nome in names:
#         nomes.append(nome[:-1])
#
# for nome in nomes:
#     with open(f"../Mail Merge Project Start/Output/ReadyToSend/carta_para_{nome}.txt", mode="w") as guest_mail:
#         guest_mail.write(f"Dear {nome},\n\nYou are invited to my birthday this Saturday.\n\nHope you can make it!\n\nAngela")


## Correção ##

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
