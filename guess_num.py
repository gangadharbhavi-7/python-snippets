"""
Python program where the user is prompted to guess a number between 1 and 100.
The program continuously provides feedback, indicating whether the guess is too high
 or too low, until the user successfully guesses the correct number.

"""

import random

number=random.randint(0,100)
while True:
    user_guess=int(input("\n Guess a number between 1 and 100: "))
    if user_guess==number:
        print("Congratulations, you guessed the number correctly!")
        break

    elif user_guess<number:
        print("Your guess is too low, try again!")

    elif user_guess>number:
        print("Your guess is too high, try again!")

    else:
        if(user_guess<0 or user_guess>0):
            print("Invalid input, please enter a number between 1 and 100")
