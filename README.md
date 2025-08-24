# Simple Banking System

A simple banking system implemented in Python with classes for `Bank`, `Customer`, and `Account`.  
This program allows you to add customers and accounts, deposit and withdraw money, and check account balances through a command-line interface.

## Features

- **Bank Management**: Create a bank and manage multiple customers.
- **Customer Management**: Add customers with unique customer numbers.
- **Account Management**: Add accounts to customers with unique account numbers and initial balances.
- **Deposit & Withdraw**: Deposit money to and withdraw money from accounts, with checks for valid input and sufficient balance.
- **Balance Inquiry**: Check the balance of any account.
- **Console UI**: User-friendly menu for interaction.

## Usage

1. **Run the script**  
   Make sure you have Python 3 installed. Save the code in a file, e.g. `banking_system.py`, then run:

   ```bash
   python banking_system.py
   ```

2. **Menu Options**

   - `c` - Add Customer  
     Enter the customer's name and a unique customer number.

   - `a` - Add Account  
     Enter the customer number (must already exist) and a new account number.

   - `b` - Check Balance  
     Enter an account number to view its balance.

   - `d` - Deposit  
     Enter an account number and the amount to deposit.

   - `w` - Withdraw  
     Enter an account number and the amount to withdraw (if sufficient funds).

   - `q` - Quit  
     Exit the banking system.

## Example Interaction

```
Welcome to the Simple Banking System!
Menu |Add Customber(c) | Add Account(a) |Balance(b)| Deposit(d) | Withdraw(w) | Quit(q) : c
Enter Name: Alice
Enter Customer Number: 101
Customber Alice Successfully Added.
Menu |Add Customber(c) | Add Account(a) |Balance(b)| Deposit(d) | Withdraw(w) | Quit(q) : a
Enter Customer Number: 101
Enter Account Number: 5001
Successfuly Added New Account, Please Enter to Continue...
Menu |Add Customber(c) | Add Account(a) |Balance(b)| Deposit(d) | Withdraw(w) | Quit(q) : d
Enter Account Number: 5001
Enter Amount to Deposit: 300
Deposit Successfully done! Please Enter to Continue...
Menu |Add Customber(c) | Add Account(a) |Balance(b)| Deposit(d) | Withdraw(w) | Quit(q) : b
Enter Account Number: 5001
Account 5001 Balance 300
Menu |Add Customber(c) | Add Account(a) |Balance(b)| Deposit(d) | Withdraw(w) | Quit(q) : q
Thank you for using our banking system. Goodbye!
```

## Code Structure

- **Bank**: Manages customers and provides methods to add customers/accounts and find accounts.
- **Customer**: Holds customer info and a list of accounts.
- **Account**: Handles account number, balance, deposits, and withdrawals.
- **User Interface**: Handles all user inputs and actions in a loop.

## Notes

- All IDs (customer and account numbers) must be positive integers.
- Balances cannot go negative; withdrawals are rejected if insufficient funds.
- The console is cleared after each action for better readability.

## License

This project is provided for educational purposes and does not include any warranty. Use and modify freely.