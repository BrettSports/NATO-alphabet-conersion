import pandas as pd

nato_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in nato_data_frame.iterrows()}

def generate_phonetic():
    user_word = input("Enter a word... if you feel comfortable doing so: ")
    try:
        user_list = [nato_dict[char.upper()] for char in user_word]
    except KeyError:
        print("Please print only words.")
        generate_phonetic()
    else:
        print(user_list)

generate_phonetic()
