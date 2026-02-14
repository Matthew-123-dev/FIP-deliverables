"""
Rock-Paper-Scissors Game
Play the classic game against the computer.
"""

import random


CHOICES = ["rock", "paper", "scissors"]


def get_computer_choice():
    """Get a random choice for the computer."""
    return random.choice(CHOICES)


def determine_winner(player_choice, computer_choice):
    """
    Determine the winner of a round.
    
    Args:
        player_choice: The player's choice
        computer_choice: The computer's choice
        
    Returns:
        'player', 'computer', or 'tie'
    """
    if player_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if winning_combinations[player_choice] == computer_choice:
        return "player"
    return "computer"


def play():
    """Play Rock-Paper-Scissors."""
    print("\n" + "="*40)
    print("  ROCK-PAPER-SCISSORS")
    print("="*40)
    print("Beat the computer in this classic game!")
    print("="*40 + "\n")
    
    player_score = 0
    computer_score = 0
    rounds = 0
    
    while True:
        print(f"\nScore - You: {player_score} | Computer: {computer_score}")
        player_input = input("Enter rock, paper, scissors (or 'quit'): ").strip().lower()
        
        if player_input == 'quit':
            break
        
        if player_input not in CHOICES:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        rounds += 1
        
        print(f"\nYou chose: {player_input}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_input, computer_choice)
        
        if result == "tie":
            print("It's a tie! ")
        elif result == "player":
            print("You win this round! ")
            player_score += 1
        else:
            print("Computer wins this round! ")
            computer_score += 1
    
    print(f"\n{'='*40}")
    print("  FINAL RESULTS")
    print(f"{'='*40}")
    print(f"Rounds played: {rounds}")
    print(f"Your score: {player_score}")
    print(f"Computer score: {computer_score}")
    
    if player_score > computer_score:
        print(" You are the champion!")
    elif computer_score > player_score:
        print(" Computer wins overall!")
    else:
        print(" It's a tie overall!")
    
    print(f"{'='*40}\n")
    return True


if __name__ == "__main__":
    play()
