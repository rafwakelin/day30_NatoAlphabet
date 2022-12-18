import pandas
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
dicionario = {row.letter: row.code for (index, row) in alphabet.iterrows()}


def spelling():
    user_word = input("What word would you like to spell phonetically? ").upper()
    try:
        nato_spelling = [dicionario[letter] for letter in user_word]
    except KeyError:
        print("Sorry, this field only accept letters")
        spelling()
    else:
        print(nato_spelling)


spelling()
