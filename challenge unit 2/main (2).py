'''Implement a class called BankAccount that represent a bank account.
The class should have private attributes for account number,account holder
name,and account balance.Include methods to deposit money,withdraw money and display balance. Write a program to create a instance of the Bankaccount class and test the Bankaccount class and deposit and withdraw functionality.'''


class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Depositeed:₹{}, New Balance:₹{}".format(amount,
                                                     self.__account_balance))
    else:
      print("Invalid deposit Amount")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdraw amount ₹{},New Balance:₹{}".format(
          amount, self.__account_balance))
    else:
      print("Invalid withdrawal Amount or Insufficient Balance")

  def display_balance(self):
    print("Account Balance for {} (Account #{}): ₹{}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))


#Create an instance of the BankAccount Class

account = BankAccount("123456789", "Christina", 10000.0)

#Test deposit and withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()
