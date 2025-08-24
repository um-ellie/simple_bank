Account
attributes:account_number, balance
methodes:get_balance(), deposit(amount), withdraw(amount)

Customer
attributes:name, customer_number, accounts
methodes:get_accounts(), add_account(account)

Bank
attributes:accounts, customers
methodes:add_customer(customer), find_account(account_number)
