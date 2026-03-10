"""
Week 6: Object Oriented Programming II - Payroll System
Demonstrates inheritance, polymorphism, and composition.
"""
from abc import ABC, abstractmethod

# ==================== PART 1: Employee Hierarchy ====================

class Employee(ABC):
    """Base class for all employees."""
    
    def __init__(self, name: str, employee_id: str, salary: float):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.payment_method = None
    
    @abstractmethod
    def calculate_bonus(self) -> float:
        """Calculate bonus - must be implemented by subclasses."""
        pass
    
    def total_compensation(self) -> float:
        return self.salary + self.calculate_bonus()
    
    def receive_payment(self):
        """Process salary payment through assigned payment method."""
        if self.payment_method is None:
            raise ValueError(f"No payment method assigned for {self.name}")
        total = self.total_compensation()
        print(f"\nProcessing payment for: {self.name}")
        print(f"  Salary: ₦{self.salary:,.2f} | Bonus: ₦{self.calculate_bonus():,.2f} | Total: ₦{total:,.2f}")
        self.payment_method.process_payment(total)
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.name} (ID: {self.employee_id})"


class Manager(Employee):
    """Manager - bonus based on team size."""
    
    def __init__(self, name: str, employee_id: str, salary: float, team_size: int = 0):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size
    
    def calculate_bonus(self) -> float:
        """20% of salary + ₦50,000 per team member."""
        return (self.salary * 0.20) + (self.team_size * 50000)


class Developer(Employee):
    """Developer - bonus based on skill level."""
    
    SKILL_LEVELS = {"junior": 0.10, "mid": 0.15, "senior": 0.25}
    
    def __init__(self, name: str, employee_id: str, salary: float, skill_level: str = "junior"):
        super().__init__(name, employee_id, salary)
        self.skill_level = skill_level.lower()
        if self.skill_level not in self.SKILL_LEVELS:
            raise ValueError(f"Invalid skill level. Choose from: {list(self.SKILL_LEVELS.keys())}")
    
    def calculate_bonus(self) -> float:
        """Junior: 10%, Mid: 15%, Senior: 25%."""
        return self.salary * self.SKILL_LEVELS[self.skill_level]


class Intern(Employee):
    """Intern - flat bonus of ₦25,000."""
    
    def __init__(self, name: str, employee_id: str, salary: float):
        super().__init__(name, employee_id, salary)
    
    def calculate_bonus(self) -> float:
        return 25000.0


# ==================== PART 2: Payment System ====================

class Payment(ABC):
    """Abstract base class for payment methods."""
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass


class CreditCardPayment(Payment):
    """Credit card payment processing."""
    
    def __init__(self, card_number: str, card_holder: str):
        self._card_last_four = card_number[-4:]
        self.card_holder = card_holder
    
    def process_payment(self, amount: float) -> bool:
        print(f"  💳 Credit card ****{self._card_last_four}: ₦{amount:,.2f} processed!")
        return True


class PayPalPayment(Payment):
    """PayPal payment processing."""
    
    def __init__(self, email: str):
        self.email = email
    
    def process_payment(self, amount: float) -> bool:
        print(f"  🅿️ PayPal ({self.email}): ₦{amount:,.2f} sent!")
        return True


class BankTransferPayment(Payment):
    """Bank transfer payment processing."""
    
    def __init__(self, bank_name: str, account_number: str):
        self.bank_name = bank_name
        self._account_last_four = account_number[-4:]
    
    def process_payment(self, amount: float) -> bool:
        print(f"  🏦 Bank transfer to {self.bank_name} ****{self._account_last_four}: ₦{amount:,.2f} initiated!")
        return True


# ==================== DEMONSTRATION ====================

def main():
    print("=" * 60)
    print("  WEEK 6: OOP II - PAYROLL SYSTEM DEMONSTRATION")
    print("=" * 60)
    
    # Create employees (inheritance)
    print("\n📋 CREATING EMPLOYEES...")
    manager = Manager("Adaeze Okonkwo", "MGR001", 9500000.00, team_size=5)
    senior_dev = Developer("Chinedu Eze", "DEV001", 8500000.00, "senior")
    junior_dev = Developer("Oluwaseun Adeyemi", "DEV002", 5500000.00, "junior")
    intern = Intern("Ngozi Nnamdi", "INT001", 3000000.00)
    
    employees = [manager, senior_dev, junior_dev, intern]
    for emp in employees:
        print(f"  - {emp}")
    
    # Assign payment methods (composition)
    print("\n💳 ASSIGNING PAYMENT METHODS...")
    manager.payment_method = CreditCardPayment("4532015112830366", "Adaeze Okonkwo")
    senior_dev.payment_method = PayPalPayment("chinedu.eze@email.com")
    junior_dev.payment_method = BankTransferPayment("First Bank", "0123456789")
    intern.payment_method = BankTransferPayment("GTBank", "0987654321")
    
    # Process payments (polymorphism)
    print("\n💰 PROCESSING PAYROLL...")
    print("-" * 50)
    total_paid = 0
    for emp in employees:
        emp.receive_payment()
        total_paid += emp.total_compensation()
    print(f"\n{'─' * 50}\nTotal disbursed: ₦{total_paid:,.2f}")
    
    # Demonstrate polymorphism
    print("\n" + "=" * 60)
    print("  POLYMORPHISM DEMONSTRATION")
    print("=" * 60)
    
    print("\nSame calculate_bonus() call, different results:")
    for emp in employees:
        print(f"  {emp.__class__.__name__:<10} {emp.name:<20} Bonus: ₦{emp.calculate_bonus():>15,.2f}")
    
    print("\nSame process_payment() call, different behaviors:")
    for payment in [CreditCardPayment("1234567890123456", "Test"), 
                    PayPalPayment("test@email.com"), 
                    BankTransferPayment("Access Bank", "1122334455")]:
        payment.process_payment(100000.00)
    
    print("\n" + "=" * 60)
    print("  DEMONSTRATION COMPLETE!")
    print("=" * 60)


if __name__ == "__main__":
    main()
