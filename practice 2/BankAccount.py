class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough balance")

    def display(self):
        print(f"{self.owner}: {self.balance}")


# Create accounts
acc1 = BankAccount("Ali", 1000)
acc2 = BankAccount("Sara", 500)
acc3 = BankAccount("Mia", 1500)

acc1.deposit(200)
acc2.withdraw(100)

acc1.display()
acc2.display()
acc3.display()
