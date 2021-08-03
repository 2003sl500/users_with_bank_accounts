class BankAccount:

    def __init__(self, interest_rate, balance = 0):
        
        self.interest_rate = interest_rate
        self.balance = float(balance)

    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount) == True:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def yield_interest(self):
        if BankAccount.can_apply_interest(self.balance) == True:
            self.balance += (self.balance * self.interest_rate)
        else:
            print("You do not have a positive balance")

        return self

    def display_account_info(self):
        print("Balance: $", self.balance)
    

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) > 0:
            return True
        else:
            return False

    @staticmethod
    def can_apply_interest(balance):
        if balance > 0:
            return True
        else:
            return False

""" daniel = BankAccount(.1, 200) 
daniel.deposit(300).deposit(200).deposit(250).withdraw(200).yield_interest().display_account_info()


print()
adrian = BankAccount(.1)
adrian.deposit(1000).deposit(500).withdraw(100).withdraw(150).withdraw(80).withdraw(200).yield_interest().display_account_info()
 """