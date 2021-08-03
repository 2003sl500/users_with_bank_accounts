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

class User:
    # delaring a class attribute (bank_name)
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        # declaring instance attributes
        self.name = name
        self.email = email_address
        self.account = BankAccount(interest_rate = 0.1, balance = 0)

danielName = "Daniel Shoemaker"
adrianName = "Adrian Acosta"
keithName = "Keith Hastings"

daniel = User(danielName, "danielshoe@charter.net")
adrian = User(adrianName, "adrian@something.com")
keith = User(keithName, "keith@something.com")

def make_deposit(self, amount):
    self.account.deposit(amount)

def make_withdrawl(self, amount):
    self.account.withdraw(amount)

def transfer_money(from_user, to_user, amount):
    make_withdrawl(from_user, amount)
    make_deposit(to_user, amount)

def display_user_balance(self):
    self.account.display_account_info()



make_deposit(daniel, 1000)
make_deposit(daniel, 250)
make_deposit(daniel, 500)
make_withdrawl(daniel, 150)
display_user_balance(daniel)

make_deposit(adrian, 1500)
make_deposit(adrian, 1000)
make_withdrawl(adrian, 300)
make_withdrawl(adrian, 125)
display_user_balance(adrian)

make_deposit(keith, 1500)
make_withdrawl(keith, 150)
make_withdrawl(keith, 100)
make_withdrawl(keith, 200)
display_user_balance(keith)

transfer_money(daniel, keith, 250)
display_user_balance(daniel)
display_user_balance(keith)