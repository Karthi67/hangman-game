#Step 1 

import random

word_list = ["aardvark", "baboon", "camel"]
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
''']


# TODO-1: Randomly choose a word from the word_list and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)
print(chosen_word)

# Initialize variables
display_word = "_" * len(chosen_word)
life = len(chosen_word)

# Display initial underscores
print(display_word)

# Game loop
for j in range(life):
    guess = input("Guess a letter: ")

    if guess in chosen_word:
        new_display_word = ""
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                new_display_word += guess
            else:
                new_display_word += display_word[i]
        display_word = new_display_word
    else:
        life-=1
        print(stage[list])
        
        print(f"Wrong guess! Lives remaining: {life}")

    # Display current state of the word
    print(display_word)

# Check if the player won or lost
if "_" not in display_word:
    print("Congratulations! You guessed the word.")
else:
    print(f"Sorry, you ran out of lives. The word was: {chosen_word}")

