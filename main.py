import pandas as pd

nato_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in nato_data_frame.iterrows()}


user_word = input("Enter a word... if you feel comfortable doing so: ")
user_list = [nato_dict[char.upper()] for char in user_word]
print(user_list)
