# class Account:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.__balance = balance

#     def debit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Added {amount} to the balance")
#         else:
#             print("Deposit amount must be positive")

#     def credit(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount} from the balance")
#         else:
#             print("Invalid withdrawal amount")

#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self, balance):
#         if isinstance(balance, (int, float)):
#             if balance >= 0:
#                 self.__balance = balance
#             else:
#                 print("Balance cannot be negative")
#         else:
#             print("Balance must be a number")

#     def __str__(self):
#         return f"Account owner: {self.owner}\nBalance: {self.__balance}"

# if __name__ == "__main__":
#     account = Account("John", 100)
#     print(account)
#     account.debit(50)
#     print(account)
#     account.credit(20)
#     print(account)
#     account.set_balance(150)
#     print(account)
#     account.set_balance(-10)
#     print(account)
#     account.set_balance("100")
#     print(account)

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def debit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount} to the balance")
        else:
            print("Deposit amount must be positive")

    def credit(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} from the balance")
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if type(balance) == int or type(balance) == float:  # noqa: E721
            if balance >= 0:
                self.__balance = balance
            else:
                print("Balance cannot be negative")
        else:
            print("Balance must be a number")

    def __str__(self):
        return f"Account owner: {self.owner}\nBalance: {self.__balance}"

if __name__ == "__main__":
    account = Account("John", 100)
    print(account)
    account.debit(50)
    print(account)
    account.credit(20)
    print(account)
    account.set_balance(150)
    print(account)
    account.set_balance(-10)
    print(account)
    account.set_balance("100")
    print(account)