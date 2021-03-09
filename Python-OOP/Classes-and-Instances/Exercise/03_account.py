class Account:
    def __init__(self, id: int, name: str, balance=0):
        self.balance = balance
        self.name = name
        self.id = id

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount > self.balance:
            return "Amount exceeded balance"

        self.balance -= amount
        return self.balance

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())

account1 = Account(5411256, "Peter")
print(account1.debit(500))
print(account1.credit(1000))
print(account1.debit(500))
print(account1.info())