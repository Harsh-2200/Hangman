import random
from words import words
import string



def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet    = set(string.ascii_uppercase)
    used_letters = set()


    #getting input
    while len(word_letters) > 0:

        #letter used
        print('You have use these letter : ' , " ".join(used_letters) )

        #current word
        word_list = [letter if letter in used_letters else '-' for letter in word ]
        print("current word ", " ".join(word_list) )


        user_letter = input("Type somthing : ").upper()


        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You already used that character .Try Again ")

hangman()




