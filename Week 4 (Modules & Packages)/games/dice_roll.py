"""
Dice Roll Game
Roll virtual dice and see the results.
"""

import random


def roll_dice(num_dice=2, sides=6):
    """
    Roll a specified number of dice.
    
    Args:
        num_dice: Number of dice to roll (default: 2)
        sides: Number of sides on each die (default: 6)
        
    Returns:
        A list of roll results
    """
    return [random.randint(1, sides) for _ in range(num_dice)]


def play():
    """Play the Dice Roll game."""
    print("\n" + "="*40)
    print("  DICE ROLL")
    print("="*40)
    print("Roll the dice and test your luck!")
    print("="*40 + "\n")
    
    while True:
        try:
            num_dice = input("How many dice to roll? (default: 2): ").strip()
            num_dice = int(num_dice) if num_dice else 2
            
            sides = input("How many sides per die? (default: 6): ").strip()
            sides = int(sides) if sides else 6
            
            if num_dice < 1 or sides < 2:
                print("Invalid input! Need at least 1 die with 2 sides.")
                continue
                
        except ValueError:
            print("Please enter valid numbers!")
            continue
        
        results = roll_dice(num_dice, sides)
        total = sum(results)
        
        print(f"\n🎲 Rolling {num_dice} dice with {sides} sides...")
        print(f"Results: {results}")
        print(f"Total: {total}")
        
        play_again = input("\nRoll again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
    
    return True


if __name__ == "__main__":
    play()
