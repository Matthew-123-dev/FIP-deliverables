"""
Guess the Number Game
Try to guess a random number between 1 and 100.
"""

import random


def play():
    """Play the Guess the Number game."""
    print("\n" + "="*40)
    print("  GUESS THE NUMBER")
    print("="*40)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")
    print("="*40 + "\n")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try higher.")
        elif guess > secret_number:
            print("Too high! Try lower.")
        else:
            print(f"\n Congratulations! You guessed it in {attempts} attempts!")
            return True
    
    print(f"\n Out of attempts! The number was {secret_number}.")
    return False


if __name__ == "__main__":
    play()
