import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
words_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

is_alphabet = False
while not is_alphabet:
    try:
        user_word = input("Enter a word: ").upper()
        output_list = [words_dict[letter] for letter in user_word]
        is_alphabet = True
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output_list)
