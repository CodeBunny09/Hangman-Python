import random
from words import words
import string
from illustration import hangman_list
from os import system, name

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(word)
    return word

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)
    alphabet = (set(string.ascii_uppercase))
    used_letters = set()
    incorrect_guesses = set()
    tries = 0
    hman = hangman_list[0]
    message = ''
    
    while len(word_letters) > 0 and tries != 8:
        word_list = [letter if letter in used_letters else '-' for letter in word]
        clear()
        print(hman)
        print(f'Letter starts with: {word[0]}')
        print(f'The word: {"".join(word_list)}')
        print(f'\nYou have used: {", ".join(used_letters)}')
        print(f'Incorrect guesses: {", ".join(incorrect_guesses)}')
        print(f'You have {8-tries} tries left.')
        print(message)
        message = ''
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                incorrect_guesses.add(user_letter)
                tries = len(incorrect_guesses)
                hman = hangman_list[tries-1]
        
        elif user_letter in used_letters:
            message = '\n\nYou already guessed that word...\tTry again!'
        else:
            message = '\n\nInvalid Guess :\'(\tTry again!'
    
    
    
    if tries < 8:
        clear()
        print(hman)
        print(f'Letter starts with: {word[0]}')
        print(f'The word: {"".join(word_list)}')
        print(f'\nYou have used: {", ".join(used_letters)}')
        print(f'Incorrect guesses: {", ".join(incorrect_guesses)}')
        print(f'You have {8-tries} tries left.')
        print(f'\n\nCongo!! You Got It!\nThe Word Was: {word}')
    else:
        clear()
        print(hman)
        print(f'Letter starts with: {word[0]}')
        print(f'The word: {"".join(word_list)}')
        print(f'\nYou have used: {", ".join(used_letters)}')
        print(f'Incorrect guesses: {", ".join(incorrect_guesses)}')
        print(f'You have {8-tries} tries left.')
        print('\n\nYou Loose...')
        print(f'The Word Was: {word}')
        
    input('Press the enter key to end <3')
        
user_input = input('Press the enter key!!')
print('\n\n')
hangman()