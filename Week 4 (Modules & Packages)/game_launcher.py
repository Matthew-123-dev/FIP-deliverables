"""
Game Launcher - Main Script
Choose and play different mini-games from the games package.
"""

from games import guess_number, dice_roll, rps


def display_menu():
    """Display the game selection menu."""
    print("\n" + "="*40)
    print("   GAME LAUNCHER ")
    print("="*40)
    print("  1. Guess the Number")
    print("  2. Dice Roll")
    print("  3. Rock-Paper-Scissors")
    print("  4. Quit")
    print("="*40)


def main():
    """Main function to run the game launcher."""
    print("\nWelcome to the Game Launcher!")
    
    while True:
        display_menu()
        choice = input("\nSelect a game (1-4): ").strip()
        
        if choice == "1":
            guess_number.play()
        elif choice == "2":
            dice_roll.play()
        elif choice == "3":
            rps.play()
        elif choice == "4":
            print("\nThanks for playing! Goodbye! \n")
            break
        else:
            print("\nInvalid choice! Please select 1-4.")


if __name__ == "__main__":
    main()
