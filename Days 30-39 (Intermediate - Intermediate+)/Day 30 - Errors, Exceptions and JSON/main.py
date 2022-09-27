import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

wrong_input = True


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Desculpe, apenas letras.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()

# Usando o tratamento de erros, impeça que o programa crash caso o usuario não digite caracteres.
