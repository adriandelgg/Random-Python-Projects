#Create a Hangman Letter guessing game.
import random
words = [
    'apple',
    'banana',
    'pear',
    'orange',
    'watermelon'
]
while True:
    start = input("Welcome! Press a key to begin or Q to quit. ").lower()
    if start == "q":
        break
    secret_word = random.choice(words)
    good_guesses = []
    bad_guesses = []
    while len(good_guesses) != len(list(secret_word)) and len(bad_guesses) < 7:
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end="")
            else:
                print('-', end='')
        print('')
        print('Strikes: {}/7'.format(len(bad_guesses))
        print('')
        guess = input("Guess a letter! ").lower()
        if len(guess) != 1:
            print('You can only guess a single letter!')
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter!")
            continue
        elif not guess.isalpha():
            print("You can only guess letters!")
            continue
        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print("You win! The word was {}.".format(secret_word))
                break
        else:
            bad_guesses.append(guess)
    else:
        print("You didn't guess it! My secret word was {}.".format(secret_word))

        
