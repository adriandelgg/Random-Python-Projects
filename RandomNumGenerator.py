#Create a random number generator guessing game.
import random
import os
#Generate random number
def random_number_game():
    secret_num = random.randint(1, 10)
    counter = 0
    while counter < 5:
        try:
            guess = int(input("Can you guess the number between 1 & 10? "))
        except ValueError:
            print("Incorrect input. Guess a number!")
            continue 
        else: 
            if guess == secret_num:
                print("You guessed it! It was {}".format(secret_num))
                play_again = input("Want to play again? \"YES\" or \"NO\": ").upper()
                if play_again != "YES" and play_again != "NO":
                    print("Incorrect input!")
                elif play_again == "YES":
                    random_number_game()
                elif play_again == "NO":
                    print("Thank you for playing!")
                    break
            elif guess > secret_num:
                print("Your guess was to high!")
                counter += 1
                continue
            elif guess < secret_num:
                print("Your guess was to low!")
                counter += 1
                continue
    else:
        play_again = input("Your ran out of guesses! Want to play again? \"YES\" or \"NO\": ").upper()
        if play_again == "YES":
            random_number_game()
        elif play_again != "YES" and play_again != "NO":
            print("Incorrect input!")
        elif play_again == "NO":
            print("Thank you for playing!")
random_number_game()