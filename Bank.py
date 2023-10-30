class Bank_Account:

  def __init__(self):
    self.balance = 0
    print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

  def deposit(self, amount):
    self.balance += amount
    print("\n Amount Deposited:", amount)

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
      print("\n You Withdrew:", amount)
    else:
      print("\n Insufficient balance  ")

  def display(self):
    print("\n Net Available Balance=", self.balance)


# creating an object of class
s = Bank_Account()

# Calling functions with that class object
s.deposit(1000)
s.withdraw(400)
s.display()
