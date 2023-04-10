"""Guessing game.

The purpose of this module is to demonstrate looping and decision structures in
a non-trial way. This was done by incrementally developing a number guessing
game.
"""
import random

# Welcome the user.
print("Let's play a game. I will think of a number between 1 and 10 and you try to guess it.")

while True:  # game loop
    secret_number = random.randint(1, 10)
    guess = -1

    while True:  # play this round of the game
        while True:  # get valid input
            try:
                guess = int(input("Please enter your guess: "))
            except ValueError:
                print("Sorry, that is not a number. Please try again.")
            else:
                if 1 <= guess <= 10:
                    break

                print("Sorry, your guess must be between 1 and 10 (inclusive). Please try again.")

        if guess == secret_number:
            break

        print("That is not the number I am thinking of. Guess again.")

    print("You guessed the secret number!!")
    again = input("Do you want to play again? (y/n) ")

    if again.lower()[0] == "n":
        break

print("Thanks for playing! Bye!")
