"""A simple banking system with classes for Bank, Customer, and Account.
Allows adding customers and accounts, depositing, withdrawing, and checking balances."""

import os

# Function to clear the console
def clear_console() :
    os.system('cls' if os.name == 'nt' else 'clear')


# Define the classes
class Account :

    """A class representing a bank account."""

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def get_balance(self) :
        return f"Account {self.account_number} Balance {self.balance}"

    def deposit(self, amount) :
        self.balance +=amount
        return True


    def withdraw(self, amount) :
        if self.balance >= amount :
            self.balance -= amount
            return True
        else :
            return False
    
    def __str__(self):
        return f"Account {self.account_number} | Balance: {self.balance}"
        

  
class Customer :

    """A class representing a bank customer."""
    
    def __init__(self, name, customer_number, accounts=None):
        self.name = name
        self.customer_number = customer_number
        self.accounts = accounts if accounts is not None else []

    def get_accounts(self) :
        customer_output = f"{self.name} with customer number {self.customer_number}:\n"
        for acc in self.accounts :
            customer_output += str(acc) + "\n"
        return customer_output
    
    def add_account(self, account_number, balance) :
        account = Account(account_number, balance)
        self.accounts.append(account)
        return account


class Bank :

    """A class representing a bank."""

    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, name, customer_number) :
        customer = Customer(name, customer_number)
        self.customers.append(customer)
        return customer
    
    def get_customer(self,customer_number) :
        for customer in self.customers :
            if customer.customer_number == customer_number :
                return customer
        return None
    
    def add_account(self, customer_number, account_number, balance=0) :
        customer = self.get_customer(customer_number)
        if customer :
            return customer.add_account(account_number, balance)
        return None
    
    def find_account(self, account_number):
        for customer in self.customers :
            for account in customer.accounts:
                if account.account_number == account_number :
                    return account
        return None



def input_positive_number(prompt) :

    """Function to get a valid positive number from user input."""

    while True :
        try :
            value = int(input(prompt))
            if value > 0 :
                return value
            else :
                print(message_dic["positive"])
        except ValueError :
                print(message_dic["invalid"])


# Dictionary for user messages

message_dic = {
    "deposit_true" : "Deposit Successfully done! Please Enter to Continue...",
    "deposit_false" : "Deposit Failed! Please Enter to Continue...",
    "withdraw_true" : "Witdraw Successfully done! Please Enter to Continue...",
    "withdraw_false" : "Withdraw Failed. Your Balance is Low! Please Enter to Continue...",
    "positive" : "Please Enter a Positive Number.",
    "invalid" : "Invalid Input, Please Enter a Valid Number.",
    "add_account_true" : "Successfuly Added New Account, Please Enter to Continue...",
    "add_account_false" : "Failed to Add New Account, Please Enter to Continue...",
}


clear_console()
print("Welcome to the Simple Banking System!")

bank = Bank("My Bank") # Create a Bank instance


"""Main loop for user interaction"""

while True:
    command = input("Menu |Add Customber(c) | Add Account(a) |Balance(b)| Deposit(d) | Withdraw(w) | Quit(q) : ").strip().lower()

    match command :
        case 'c' : # Add Customer
            name = input("Enter Name:")
            cuts_no = input_positive_number("Enter Customer Number:")
            bank.add_customer(name, cuts_no)
            print(f"Customber {name} Successfully Added.")
            input("Please Enter to Continue...")

        case 'a' : # Add Account
            cust_no = input_positive_number("Enter Customer Number:")
            acc_no = input_positive_number("Enter Account Number:")
            account = bank.add_account(cust_no,acc_no, 0)

            if account :
                input(message_dic["add_account_true"])
            else :
                input(message_dic["add_account_false"])

        case 'b' : # Check Balance
            acc_no = input_positive_number("Enter Account Number:")
            account = bank.find_account(acc_no)
            if account :
                print(account.get_balance())
            else :
                print("Account Not Found!")

        case 'd' : # Deposit
            acc_no = input_positive_number("Enter Account Number:")
            account = bank.find_account(acc_no)
            if account : 
                amount = input_positive_number("Enter Amount to Deposit:")
                if account.deposit(amount) :
                    input(message_dic["deposit_true"])
            else :
                input("Account Not Found!")

        case 'w' : # Withdraw
            acc_no = input_positive_number("Enter Account Number:")
            account = bank.find_account(acc_no)
            if account : 
                amount = input_positive_number("Enter Amount to Withdraw:")
                if account.withdraw(amount) :
                    input(message_dic["withdraw_true"])
                else:
                    input(message_dic["withdraw_false"])
            else: 
                print("Account Not Found!")

        case 'q' : # Quit
            print("Thank you for using our banking system. Goodbye!")
            break

        case _ : # Invalid Input
            print(message_dic["invalid"])