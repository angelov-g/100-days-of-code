import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ")
nato_list = [alphabet_dict[letter.upper()] for letter in user_input]
print(nato_list)
