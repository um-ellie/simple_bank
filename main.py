
"""A simple banking system with customers and accounts."""

import os
import json
from pathlib import Path
from typing import List, Optional

DATA_FILE = Path("bank_data.json")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


class Account:
    """A class representing a bank account."""

    def __init__(self, account_number: int, balance: float = 0.0):
        self.account_number = int(account_number)
        self.balance = float(balance)

    def get_balance(self):
        """Get the current balance of the account."""
        return f"Account {self.account_number} Balance: {self.balance:.2f}"

    def deposit(self, amount: float) -> bool:
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def to_dict(self) -> dict:
        return {
            "account_number": self.account_number,
            "balance": self.balance,
        }

    @staticmethod
    def from_dict(data: dict) -> "Account":
        return Account(data["account_number"], data.get("balance", 0.0))

    def __str__(self):
        return f"Account {self.account_number} | Balance: {self.balance:.2f}"


class Customer:
    """A class representing a bank customer."""

    def __init__(self, name: str, customer_number: int, accounts: Optional[List[Account]] = None):
        self.name = name
        self.customer_number = int(customer_number)
        self.accounts: List[Account] = accounts if accounts is not None else []

    def get_accounts(self) -> str:
        """Get a list of all accounts for the customer."""
        customer_output = f"{self.name} with customer number {self.customer_number}:\n"
        total_balance = 0
        for acc in self.accounts:
            customer_output += str(acc) + "\n"
            total_balance += acc.balance
        customer_output += f"Total Balance: {total_balance:.2f}"
        return customer_output

    def add_account(self, account_number: int, balance: float = 0.0) -> Optional[Account]:
        """Add a new account for the customer, prevent duplicate account numbers."""
        for acc in self.accounts:
            if acc.account_number == account_number:
                return None  # Prevent duplicate
        account = Account(account_number, balance)
        self.accounts.append(account)
        return account

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "customer_number": self.customer_number,
            "accounts": [acc.to_dict() for acc in self.accounts],
        }

    @staticmethod
    def from_dict(data: dict) -> "Customer":
        accounts = [Account.from_dict(a) for a in data.get("accounts", [])]
        return Customer(data["name"], data["customer_number"], accounts)


class Bank:
    """A class representing a bank."""

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []

    def add_customer(self, name: str, customer_number: int) -> Optional[Customer]:
        """Add a new customer to the bank."""

        if self.get_customer(customer_number):
            return None  # Prevent duplicate customer numbers

        customer = Customer(name, customer_number)
        self.customers.append(customer)
        return customer

    def get_customer(self, customer_number: int) -> Optional[Customer]:
        """Get a customer by their customer number."""
        for customer in self.customers:
            if customer.customer_number == customer_number:
                return customer
        return None

    def add_account(self, customer_number: int, account_number: int, balance: float = 0.0) -> Optional[Account]:
        """Add a new account for a customer, prevent duplicate account numbers globally."""
        # Prevent duplicate account numbers globally
        if self.find_account(account_number):
            return None
        customer = self.get_customer(customer_number)
        if customer:
            return customer.add_account(account_number, balance)
        return None

    def find_account(self, account_number: int) -> Optional[Account]:
        """Find an account by its account number."""
        for customer in self.customers:
            for account in customer.accounts:
                if account.account_number == account_number:
                    return account
        return None

    def get_customers(self) -> List[Customer]:
        """Get a list of all customers in the bank."""
        return self.customers

    def get_total_balance(self) -> float:
        """Get the total balance of all customers in the bank."""
        total = sum(acc.balance for cust in self.customers for acc in cust.accounts)
        return total

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "customers": [cust.to_dict() for cust in self.customers],
        }

    def save_to_file(self, filename: Path = DATA_FILE) -> bool:
        """Persist the bank data to a JSON file."""
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(self.to_dict(), f, indent=2)
            return True
        except Exception as e:
            # for debugging in case of file system issues
            print(f"Failed to save data: {e}")
            return False

    @staticmethod
    def load_from_file(filename: Path = DATA_FILE) -> Optional["Bank"]:
        """Load bank data from a JSON file. Returns a Bank instance or None on error."""
        if not filename.exists():
            return None
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            bank = Bank(data.get("name", "My Bank"))
            for custdata in data.get("customers", []):
                cust = Customer.from_dict(custdata)
                bank.customers.append(cust)
            return bank
        except Exception as e:
            print(f"Failed to load data: {e}")
            return None


def input_positive_number(prompt: str) -> int:
    """Function to get a valid positive number from user input."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print(message_dic["positive"])
        except ValueError:
            print(message_dic["invalid"])


def show_menu() -> str:
    """Function to display the menu options."""
    print("\n" + "=" * 30)
    print("Simple Banking System")
    print("=" * 30)
    print(" [c] Add Customer")
    print(" [a] Add Account")
    print(" [b] Balance")
    print(" [d] Deposit")
    print(" [w] Withdraw")
    print(" [l] List Customers")
    print(" [q] Quit")
    print("=" * 30)
    return input("Choose an option: ").strip().lower()


# Dictionary for user messages
message_dic = {
    "deposit_true": "Deposit Successfully done! Press Enter to Continue...",
    "deposit_false": "Deposit Failed! Press Enter to Continue...",
    "withdraw_true": "Withdraw Successfully done! Press Enter to Continue...",
    "withdraw_false": "Withdraw Failed. Your Balance is Low! Press Enter to Continue...",
    "positive": "Please Enter a Positive Number.",
    "invalid": "Invalid Input, Please Enter a Valid Number.",
    "add_account_true": "Successfully Added New Account. Press Enter to Continue...",
    "add_account_false": "Failed to Add New Account (maybe duplicate number). Press Enter to Continue...",
    "account_not_found": "Account Not Found! Press Enter to Continue...",
    "customer_not_found": "Customer Not Found! Press Enter to Continue...",
    "existing_customer": "Customer Number Already Exists! Press Enter to Continue...",
}

clear_console()
print("Welcome to the Simple Banking System!")


def main() -> None:
    # Try to load saved bank data, otherwise create a fresh bank
    bank = Bank.load_from_file() or Bank("My Bank")
    if DATA_FILE.exists():
        print(f"Loaded data from {DATA_FILE}")
    else:
        print("No saved data found. Starting with a new bank.")

    while True:
        command = show_menu()

        match command:
            case 'c':  # Add Customer
                name = input("Enter Name:")
                cust_no = input_positive_number("Enter Customer Number:")
                cust = bank.add_customer(name, cust_no)
                if cust:
                    # Persist change
                    bank.save_to_file()
                    print(f"\nCustomer {name} Successfully Added.")
                else:
                    print(message_dic["existing_customer"])
                input("Press Enter to Continue...")
                clear_console()

            case 'a':  # Add Account
                cust_no = input_positive_number("Enter Customer Number:")
                acc_no = input_positive_number("Enter Account Number:")
                account = bank.add_account(cust_no, acc_no, 0)
                if account:
                    bank.save_to_file()
                    input(message_dic["add_account_true"])
                    clear_console()
                else:
                    input(message_dic["add_account_false"])
                    clear_console()

            case 'b':  # Check Balance
                cust_no = input_positive_number("Enter Customer Number:")
                customer = bank.get_customer(cust_no)
                if customer:
                    print(customer.get_accounts())
                    input("Press Enter to Continue...")
                    clear_console()
                else:
                    input(message_dic["customer_not_found"])
                    clear_console()

            case 'd':  # Deposit
                acc_no = input_positive_number("Enter Account Number:")
                account = bank.find_account(acc_no)
                if account:
                    amount = input_positive_number("Enter Amount to Deposit:")
                    if account.deposit(amount):
                        # Persist change
                        bank.save_to_file()
                        input(message_dic["deposit_true"])
                        clear_console()
                    else:
                        input(message_dic["deposit_false"])
                        clear_console()
                else:
                    input(message_dic["account_not_found"])
                    clear_console()

            case 'w':  # Withdraw
                acc_no = input_positive_number("Enter Account Number:")
                account = bank.find_account(acc_no)
                if account:
                    amount = input_positive_number("Enter Amount to Withdraw:")
                    if account.withdraw(amount):
                        # Persist change
                        bank.save_to_file()
                        input(message_dic["withdraw_true"])
                        clear_console()
                    else:
                        input(message_dic["withdraw_false"])
                        clear_console()
                else:
                    input(message_dic["account_not_found"])
                    clear_console()

            case 'l':  # List Customers
                customers = bank.get_customers()
                if customers:
                    print("List of Customers:\n")
                    for cust in customers:
                        print(cust.get_accounts())
                        print("-" * 30)
                    print("*" * 30)
                    print(f"Total Customers: {len(customers)}")
                    print(f"Total Balance in Bank: {bank.get_total_balance():.2f}")
                else:
                    print("No Customers Found!")
                input("\nPress Enter to Continue...")
                clear_console()

            case 'q':  # Quit
                print("Thank you for using our banking system. Goodbye!")
                break

            case _:  # Invalid Input
                print(message_dic["invalid"])


if __name__ == "__main__":
    main()