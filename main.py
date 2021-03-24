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
correct_word_list_unchanged = []
underlines = []
wrong_count = []

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
        correct_word_list_unchanged.append(i)
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
    get_random_word()
    word_to_list()
    generate_underlines()

    while True:
        # Check if game over or won
        if len(wrong_count) == 6:
            game_over()
            break
        if len(correct_word_list) == 0:
            game_won()
            break

        # Printing the state of the hung man
        print(hangman_states[len(wrong_count)])

        # Printing status
        guessstatus = ''.join(underlines)
        print(guessstatus)

        # Lets you guess
        guess = str(input("Guess Letter: "))
        if guess in correct_word_list:
            print(f"Correct: {guess}")
            index = correct_word_list_unchanged.index(guess)
            underlines[index] = guess
            correct_word_list.remove(guess)
        else:
            print("Guess again")
            wrong_count.append("X")
        clear()

if __name__ == '__main__':
    main()
