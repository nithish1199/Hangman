import random
from words import word
import string


def valid_word(word):
    w = random.choice(word)
    while '-' in w or ' ' in w:
        w = random.choice(word)
    return w


def hangman():
    w = valid_word(word).upper()
    w_letters = set(w)
    alpha = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    while len(w_letters) > 0 and lives > 0:
        print('You have ', lives, 'lives left')
        print('You have used these words ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in w]
        print('Current word ', ' '.join(word_list))
        user_letter = input('Type a letter ').upper()
        if user_letter in alpha-used_letters:
            used_letters.add(user_letter)
            if user_letter in w_letters:
                w_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter ', user_letter, ' is not in word')
        elif user_letter in used_letters:
            print('You have already used this character . Please try another')
        else:
            print('Invalid character.Please try again')
    if lives == 0:
        print('Sorry,you died. The word was', w)
    else:
        print('You guess the word ', word, ' yay!!!')


hangman()
