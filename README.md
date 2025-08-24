# simple_bank

A tiny, single-file CLI banking demo in Python: customers, accounts, deposits, withdrawals, and JSON persistence.

Requirements
- Python 3.8+

Quick start
1. Clone the repo:
   git clone https://github.com/um-ellie/simple_bank.git
2. Run:
   python main.py

Menu (single-letter commands)
- c — Add Customer (name + positive integer customer number)
- a — Add Account (customer number + positive integer account number)
- b — View Balance (shows a customer's accounts & total)
- d — Deposit (account number + positive amount)
- w — Withdraw (account number + positive amount, must have funds)
- l — List Customers (summary of all customers)
- q — Quit

Data
- All data is saved to bank_data.json in the repo root when changes are made.
- Example structure:
```json
{
  "name": "My Bank",
  "customers": [
    {"name":"Alice","customer_number":1,"accounts":[{"account_number":100,"balance":2500.0}]}
  ]
}
```

Notes & small caveats
- The app uses Python floats for balances (easy to read/demo). For production or precise money handling, switch to Decimal or store cents as integers.
- Customer and account numbers must be positive integers.
- Deposits and withdrawals are validated as positive numbers and withdrawals require sufficient balance.
- No authentication: this is an educational demo.

Examples (quick flow)
- Add customer: choose `c`, enter `Alice`, enter `1`
- Add account: choose `a`, enter `1` (customer), enter `100` (account)
- Deposit: choose `d`, enter `100`, enter `500`
- Withdraw: choose `w`, enter `100`, enter `200`
- List: choose `l` to see customers and totals

Testing & improvements
- There are no automated tests. Suggested next steps: add pytest unit tests for Account, Customer, and Bank logic; use Decimal for money; add a basic CI workflow.

License
- This project is dedicated to the public domain (see LICENSE). Use it freely.

Author / Repo
- https://github.com/um-ellie/simple_bank
