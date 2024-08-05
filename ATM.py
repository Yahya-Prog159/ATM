# withdraw ==> سحب
# Deposit ==> ايداع
balance = int(input("Enter your balance : "))
amount = int(input("Enter the amount : "))
class ATM :
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f'Your balance is : {self.balance}')

    def withdraw(self,amount):
        self.balance -= amount
        print(f'Your balance : {self.balance}')

x = ATM(balance)
x.deposit(amount)
x.withdraw(amount)


# ____________________________________________


# withdraw ==> سحب
# Deposit ==> ايداع


# balance = int(input("Enter your balance : "))
# op = input("Withdraw or Deposit : ").lower()
# amount = int(input("Enter the amount that will be applied on the deposit or withdraw : "))
#
#
# class ATM :
#     def __init__(self, balance):
#         self.balance = balance
#
#         if op == "deposit":
#             self.balance += amount
#             print(f'Your balance : {self.balance}')
#         elif op == "withdraw":
#             self.balance -= amount
#             print(f'Your balance : {self.balance}')
#
#
# x = ATM(balance)
