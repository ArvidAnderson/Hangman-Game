#Simple Hangman Game by Arvid Anderson
#https://github.com/ArvidAnderson?

import random
from os import system, name
# Hangman States
hangman_states = ['''






=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Arrays

words = []
correct_word = []
correct_word_list = []
underlines = []
wrong_count = []
right_count = []

#Functions

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def get_random_word():
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    correct_word.append(random.choice(words))


def generate_underlines():
    for i in correct_word_list:
        underlines.append('_')


def word_to_list():
    for i in correct_word[0]:
        correct_word_list.append(i)
    return correct_word_list

def game_over():
    print(hangman_states[7])
    print("Game Over")
    print("=========")


def game_won():
    print("=======")
    print("You Won")
    print("=======")


def main():
    #Functions required to setup the diff arrays
    get_random_word()
    word_to_list()
    generate_underlines()

    while True:
        #Checks if game is done or not
        if len(wrong_count) == 6:
            game_over()
            break

        #Checks if INSERTEDBYPROGRAM is in whole list if so you win
        result = False
        if len(correct_word_list) > 0 :
            result = correct_word_list.count(correct_word_list[0]) == len(correct_word_list)

        if result == True:
            game_won()
            break

        # Printing state of the man, gets state from wrong_count array
        print(hangman_states[len(wrong_count)])

        # Prints the status of the word
        guessstatus = ''.join(underlines)
        print(guessstatus)

        # Lets you guess
        guess = str(input("Guess Letter: ")).lower()
        #Checks if inputed letter in list and if so prints correct and removes from the list

        if guess in correct_word_list:
            print(f"Correct: {guess}")
            index = correct_word_list.index(guess)
            underlines[index] = guess
            correct_word_list[index] = 'INSERTEDBYPROGRAM'
            right_count.append("X")
        #Lets you guess again and adds an X to the wrong_count array
        else:
            print("Guess again")
            wrong_count.append("X")
        clear()
#Runs main() on start
if __name__ == '__main__':
    main()
