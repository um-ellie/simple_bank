"""A simple banking system with classes for Bank, Customer, and Account.
Allows adding customers and accounts, depositing, withdrawing, and checking balances."""

import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Account:
    """A class representing a bank account."""

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def get_balance(self):
        """Get the current balance of the account."""
        return f"Account {self.account_number} Balance: {self.balance:.2f}"

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Account {self.account_number} | Balance: {self.balance:.2f}"

class Customer:
    """A class representing a bank customer."""

    def __init__(self, name, customer_number, accounts=None):
        self.name = name
        self.customer_number = customer_number
        self.accounts = accounts if accounts is not None else []

    def get_accounts(self):
        """Get a list of all accounts for the customer."""
        customer_output = f"{self.name} with customer number {self.customer_number}:\n"
        total_balance = 0
        for acc in self.accounts:
            customer_output += str(acc) + "\n"
            total_balance += acc.balance
        customer_output += f"Total Balance: {total_balance:.2f}"
        return customer_output

    def add_account(self, account_number, balance):
        """Add a new account for the customer, prevent duplicate account numbers."""
        for acc in self.accounts:
            if acc.account_number == account_number:
                return None  # Prevent duplicate
        account = Account(account_number, balance)
        self.accounts.append(account)
        return account

class Bank:
    """A class representing a bank."""

    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, name, customer_number):
        """Add a new customer to the bank."""
        customer = Customer(name, customer_number)
        self.customers.append(customer)
        return customer

    def get_customer(self, customer_number):
        """Get a customer by their customer number."""
        for customer in self.customers:
            if customer.customer_number == customer_number:
                return customer
        return None

    def add_account(self, customer_number, account_number, balance=0):
        """Add a new account for a customer, prevent duplicate account numbers globally."""
        # Prevent duplicate account numbers globally
        if self.find_account(account_number):
            return None
        customer = self.get_customer(customer_number)
        if customer:
            return customer.add_account(account_number, balance)
        return None

    def find_account(self, account_number):
        """Find an account by its account number."""
        for customer in self.customers:
            for account in customer.accounts:
                if account.account_number == account_number:
                    return account
        return None
    
    def get_customers(self):
        """Get a list of all customers in the bank."""
        return self.customers


def input_positive_number(prompt):
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

def show_menu():
    """Function to display the menu options."""
    print("\n" + "="*30)
    print("Simple Banking System")
    print("="*30)
    print(" [c] Add Customer")
    print(" [a] Add Account")
    print(" [b] Balance")
    print(" [d] Deposit")
    print(" [w] Withdraw")
    print(" [l] List Customers")
    print(" [q] Quit")
    print("="*30)
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
    "customer_not_found": "Customer Not Found! Press Enter to Continue..."
}

clear_console()
print("Welcome to the Simple Banking System!")

def main() -> None:
    bank = Bank("My Bank")  # Create a Bank instance
    while True:
        command = show_menu()

        match command:
            case 'c':  # Add Customer
                name = input("Enter Name:")
                cust_no = input_positive_number("Enter Customer Number:")
                bank.add_customer(name, cust_no)
                print(f"Customer {name} Successfully Added.")
                input("Press Enter to Continue...")
                clear_console()

            case 'a':  # Add Account
                cust_no = input_positive_number("Enter Customer Number:")
                acc_no = input_positive_number("Enter Account Number:")
                account = bank.add_account(cust_no, acc_no, 0)
                if account:
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
                        input(message_dic["deposit_true"])
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
                        print("-"*30)
                else:
                    print("No Customers Found!")
                input("Press Enter to Continue...")
                clear_console()

            case 'q':  # Quit
                print("Thank you for using our banking system. Goodbye!")
                break
            
            case _:  # Invalid Input
                print(message_dic["invalid"])

if __name__ == "__main__":
    main()