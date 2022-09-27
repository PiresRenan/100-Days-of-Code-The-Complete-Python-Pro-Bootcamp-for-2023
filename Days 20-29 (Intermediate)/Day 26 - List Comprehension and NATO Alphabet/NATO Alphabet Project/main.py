import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())
# TO DO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

# TO DO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
