# Week 6: Object Oriented Programming II

## Payroll System with Multiple Payment Methods

This program demonstrates advanced OOP concepts by modeling an organization's payroll system where employees receive salaries through different payment methods.

## Concepts Covered

- **Inheritance** - Employee subclasses extend a base class
- **Polymorphism** - Same method calls produce different behaviors
- **Abstraction** - Abstract base classes define interfaces
- **Composition** - Employees contain payment method objects

## Project Structure

### Part 1: Employee Hierarchy

| Class | Description | Bonus Calculation |
|-------|-------------|-------------------|
| `Employee` | Abstract base class | Abstract method |
| `Manager` | Manages a team | 20% salary + ₦50,000 per team member |
| `Developer` | Technical staff | Junior: 10%, Mid: 15%, Senior: 25% |
| `Intern` | Entry-level | Flat ₦25,000 |

### Part 2: Payment System

| Class | Description |
|-------|-------------|
| `Payment` | Abstract base class |
| `CreditCardPayment` | Processes credit card payments |
| `PayPalPayment` | Processes PayPal transfers |
| `BankTransferPayment` | Processes bank transfers |

## How to Run

```bash
python app.py
```

## Sample Output

```
============================================================
  WEEK 6: OOP II - PAYROLL SYSTEM DEMONSTRATION
============================================================

📋 CREATING EMPLOYEES...
  - Manager: Adaeze Okonkwo (ID: MGR001)
  - Developer: Chinedu Eze (ID: DEV001)
  - Developer: Oluwaseun Adeyemi (ID: DEV002)
  - Intern: Ngozi Nnamdi (ID: INT001)

💰 PROCESSING PAYROLL...
--------------------------------------------------

Processing payment for: Adaeze Okonkwo
  Salary: ₦9,500,000.00 | Bonus: ₦2,150,000.00 | Total: ₦11,650,000.00
  💳 Credit card ****0366: ₦11,650,000.00 processed!
```

## Key Takeaways

1. **Inheritance** allows code reuse - all employee types share common attributes and methods
2. **Polymorphism** enables flexibility - `calculate_bonus()` and `process_payment()` behave differently per subclass
3. **Composition** integrates systems - employees are assigned payment methods as objects
