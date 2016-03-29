#!/usr/bin/env python

# tutorial on encapsulation (object oriented programming) from https://www.youtube.com/watch?v=5oeitr6fBBQ

'''
class bankAccount():
    # This is a bank account class
    def __init__(self, account_name = "Current Account", balance = 200):
        self.account_name = account_name
        self.balance = balance

accountObject = bankAccount()

print(accountObject.account_name)
print(accountObject.balance)

input()
'''

'''
The above code prints the following to the screen:
Current Account
200

To make the attributes private, you can put double underscores in front of account_name and balance, like this:
self.__account_name = account_name
self.__balance = balance

This is important because you could override the account balance for a crazy amount, like this:
accountObject.balance = 200000000
and then the value has been changed...
but if you can make the attributes private, then the account is secure.

However, we can use getters and setters if we still want to make the attributes private but still want to access them in a particular way.
'''

# Here is an example of getters and setters:

class bankAccount():
    # This is a bank account class
    def __init__(self, account_name = "Current Account", balance = 200):
        self.__account_name = account_name
        self.__balance = balance
    
    def balanceGetter(self):
        print(self.__balance)
    
    def balanceSetter_withdraw(self, value):
        if value < self.__balance:
            self.__balance = self.__balance - value
            print("New Balance: ", self.__balance)
        else:
            print("You do not have enough funds!")
            
accountObject = bankAccount()

while True:
    print("1. Check Account Balance")
    print("2. Withdraw funds")
    menu_option = int(input())
    if menu_option == 1:
        value = int(input("How much would you like to withdraw? "))
        accountObject.balanceSetter_withdraw(value)
    else:
        print("Wrong menu choice!")

print(accountObject.account_name)
print(accountObject.balance)

input()