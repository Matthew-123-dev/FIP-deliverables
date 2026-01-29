# Bank Withdrawal System

A simple Python program that simulates a bank withdrawal system, demonstrating error handling using `try`, `except`, `else`, and `finally` blocks.

## Overview

This program allows users to withdraw money from a virtual bank account with a starting balance of ₦100,000. It validates user input and handles various error scenarios gracefully.

## Features

- Interactive withdrawal system with user input
- Input validation for invalid and negative amounts
- Insufficient funds detection
- Transaction logging after each attempt
- Running balance display

## Exception Handling Demonstration

| Block | Purpose |
|-------|---------|
| `try` | Attempts to convert user input and validate the withdrawal amount |
| `except ValueError` | Handles invalid input (non-numeric values or negative amounts) |
| `except Exception` | Handles insufficient funds errors |
| `else` | Executes on successful withdrawal, updates and displays the new balance |
| `finally` | Always runs to log the transaction, regardless of success or failure |

## How to Run

```bash
python app.py
```

## Example Usage

```
==================================================
       WELCOME TO THE BANK WITHDRAWAL SYSTEM
==================================================

Your current balance: ₦100,000.00

--------------------------------------------------
Enter withdrawal amount (or 'quit' to exit): ₦5000

✅ Withdrawal Successful!
   Amount withdrawn: ₦5,000.00
   New balance: ₦95,000.00

📝 Transaction logged.
--------------------------------------------------
Enter withdrawal amount (or 'quit' to exit): ₦quit

Thank you for using our banking system!

Final Balance: ₦95,000.00
==================================================
```

## Requirements

- Python 3.x
