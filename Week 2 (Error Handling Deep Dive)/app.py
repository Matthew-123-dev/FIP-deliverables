"""
Bank Withdrawal System
Demonstrates exception handling with try, except, else, and finally blocks.
"""

def bank_withdrawal_system():
    """Main function to run the bank withdrawal simulation."""
    balance = 100000  # Starting balance in Naira
    
    print("=" * 50)
    print("       WELCOME TO THE BANK WITHDRAWAL SYSTEM")
    print("=" * 50)
    print(f"\nYour current balance: ₦{balance:,.2f}\n")
    
    while True:
        print("-" * 50)
        user_input = input("Enter withdrawal amount (or 'quit' to exit): ₦")
        
        if user_input.lower() == 'quit':
            print("\nThank you for using our banking system!")
            break
        
        try:
            amount = float(user_input)
            
            # Validate the withdrawal amount
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            elif amount > balance:
                raise Exception(f"Insufficient funds! You tried to withdraw ₦{amount:,.2f} but your balance is ₦{balance:,.2f}")
            
        except ValueError:
            print("\n❌ Error: Please enter a valid positive number.")
            
        except Exception as e:
            print(f"\n❌ Transaction Declined: {e}")
            
        else:
            # Successful withdrawal - only runs if no exception occurred
            balance = balance - amount
            print(f"\n✅ Withdrawal Successful!")
            print(f"   Amount withdrawn: ₦{amount:,.2f}")
            print(f"   New balance: ₦{balance:,.2f}")
            
        finally:
            # Always runs - log the transaction
            print("\n📝 Transaction logged.")
    
    print(f"\nFinal Balance: ₦{balance:,.2f}")
    print("=" * 50)


if __name__ == "__main__":
    bank_withdrawal_system()
