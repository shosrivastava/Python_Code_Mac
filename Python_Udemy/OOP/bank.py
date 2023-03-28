print("Welcome, this code emulates a banking system.\n")

class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount > self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, there is not enough fund in this account!\n")

    def statement(self):
        print(f"The Account Balance is {self.balance}.\n")

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)

    def __str__(self):
        return "{}'s Current Account balance is {}".format(self.name, self.balance)

class Savings(Account):
    def __init__(name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return "{}'s Saving Account balance is {}".format(self.name, self.balance)

# Making objects of the above classes.

S = Current("XYZ", 500)

(S.statement())