import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    user_input = input("Enter a word: ")
    try:
        nato_list = [alphabet_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(nato_list)
        break


# ANGELA'S RECURSION (Recursion)
# def generate_phonetic():
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [alphabet_dict[letter] for letter in user_input]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         generate_phonetic()
#     else:
#         print(nato_list)
#         
# generate_phonetic()
