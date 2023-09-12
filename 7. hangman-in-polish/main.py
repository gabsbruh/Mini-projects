#-*- coding: utf-8 -*-
import random

# add stages of hangman to a game
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''

      |
      |
      |
      |
      |
=========
''', '''

      
      
      
      
      
=========
''',"""
      _.-'''''-._
    .'  _     _  '.
       (_)   (_)   
  |  ,           ,  |
  |  \`.       .`/  |
   \  '.`'""'"`.'  /
    '.  `'---'`  .'
      '-._____.-'
"""
]


# Read list of words from a file and assigning it to a list called words_list
with open('words.txt', encoding = 'utf-8') as f:
    words_list = f.read().splitlines()

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(words_list)

# number of lives equal to stages
lives = 9

# list contains letters already used
letters_used = []

# Create an empty List called display, with number of '_ ' equal to chars in a chose_word. 
display = list('_ ' * len(chosen_word))


# loop while that ends when u finally reach full word
while '_' in display:
    
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Which letter are you guessing?\n").lower()
    letters_used.append(guess)
    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word and add to a display in proper places.
    is_letter_in = True if guess in chosen_word else False
    if is_letter_in == True:
        print('\nRIGHT!!')
        print(stages[lives-1])
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[2*i] = guess # display index doubled due to spaces between underscores
        display_in_str = ''.join(display)
        print(display_in_str)
    else:
        print('\nWRONG..')
        lives -= 1
        print(f'lives left: {lives}')
        print(stages[lives-1])  # -1 cuz index starts at 0\
    # print letters used
    print('letters which you used: ' + ', '.join(letters_used))  
      
    # conditions to end a game
    if lives == 0:
        print("*** YOU LOOSE *** \t")
        break
    elif '_' not in display:
        print("*** Y O U  W I N ! *** \t")
        break
    else:
        continue
    