import random

word_list = ["ardvark", "aboon", "amel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

random.shuffle(word_list)
chosen_word = str(random.choice(word_list))

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = str(input("Ingresa una letra: ")).lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("right")
    else: 
        print("wrong")