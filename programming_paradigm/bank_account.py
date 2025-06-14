class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
    
    def deposit(self,amount):
        if amount> 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.2f}")
            print(f"New balance: ${self.account_balance:.2f}")
            return True 
        return False
    def withdraw(self, amount):
        self.account_balance -= amount
        if 0 < amount <= self.account_balance:
            print(f"Withdrawing: ${amount:.2f}")
            print(f"New balance: ${self.account_balance:.2f}")
            
            return True
        return False
    def display_balance(self):
        return f"Current Balance: ${self.account_balance:.2f}"
    