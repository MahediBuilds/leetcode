class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balnce(self):
        print(self.balance)


account = BankAccount("Zain", 1000)

account.deposit(500)
account.withdraw(200)
account.display_balance()
