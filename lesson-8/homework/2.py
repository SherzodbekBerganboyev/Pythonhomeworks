import json
import random

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_dict(self):
        return {
            'account_number': self.account_number,
            'name': self.name,
            'balance': self.balance
        }

class Bank:
    def __init__(self, filename="accounts.txt"):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()

    def generate_account_number(self):
        while True:
            number = str(random.randint(100000, 999999))
            if number not in self.accounts:
                return number

    def create_account(self, name, initial_deposit):
        account_number = self.generate_account_number()
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Account created! Your account number is {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Balance: ${account.balance:.2f}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Invalid amount. Must be positive.")
            return
        account = self.accounts.get(account_number)
        if account:
            account.balance += amount
            self.save_to_file()
            print(f"Deposited ${amount:.2f}. New balance: ${account.balance:.2f}")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            print("Account not found.")
            return
        if amount <= 0:
            print("Invalid amount. Must be positive.")
            return
        if amount > account.balance:
            print("Insufficient funds.")
            return
        account.balance -= amount
        self.save_to_file()
        print(f"Withdrew ${amount:.2f}. New balance: ${account.balance:.2f}")

    def save_to_file(self):
        with open(self.filename, 'w') as f:
            data = {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
            json.dump(data, f)

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for acc_num, acc_data in data.items():
                    self.accounts[acc_num] = Account(**acc_data)
        except FileNotFoundError:
            pass


# Bankni ishga tushirish uchun misol
if __name__ == "__main__":
    bank = Bank()
    while True:
        print("\nOptions: 1) Create Account 2) View Account 3) Deposit 4) Withdraw 5) Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter your name: ")
            try:
                initial_deposit = float(input("Enter initial deposit: "))
            except ValueError:
                print("Invalid input for deposit.")
                continue
            bank.create_account(name, initial_deposit)
        elif choice == '2':
            acc_num = input("Enter account number: ")
            bank.view_account(acc_num)
        elif choice == '3':
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to deposit: "))
            except ValueError:
                print("Invalid input for amount.")
                continue
            bank.deposit(acc_num, amount)
        elif choice == '4':
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to withdraw: "))
            except ValueError:
                print("Invalid input for amount.")
                continue
            bank.withdraw(acc_num, amount)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
