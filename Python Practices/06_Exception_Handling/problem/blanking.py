class MinimValueError(Exception):
    """Minimum value is not allowed to be less than 500"""
    pass


class Account:
    def __init__(self, owner, account_no, balance, pin):
        self.owner = owner
        self.account_no = account_no
        self._balance = balance
        self._pin = pin

        self.menu = {
            "1": "Deposit",
            "2": "Withdraw",
            "3": "Change PIN",
            "4": "Reset PIN",
            "5": "Check Balance",
            "6": "Exit"
        }

    def verify_pin(self, pin):
        """Verify if the entered pin is correct"""
        return pin == self._pin

    def change_pin(self, old_pin, new_pin):
        """Change pin after verifying old pin"""
        if not self.verify_pin(old_pin):
            return "Invalid old pin"
        self._pin = new_pin
        return "Pin changed successfully"

    def reset_pin(self, new_pin):
        """Admin or system reset (no old pin required)"""
        self._pin = new_pin
        return "Pin reset successful"

    @property
    def balance(self):
        """Return current balance (without pin check)"""
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 500:
            raise MinimValueError("Balance cannot be less than 500")
        self._balance = amount

    def check_balance(self, pin):
        """Return balance only if pin is correct"""
        if not self.verify_pin(pin):
            return "Invalid PIN"
        return f"Your current balance is: {self._balance}"

    def deposit(self, amount):
        if amount < 500:
            raise MinimValueError("Deposit amount must be at least 500")
        self._balance += amount
        return f"Deposit successful! New balance: {self._balance}"

    def withdraw(self, amount, pin):
        if not self.verify_pin(pin):
            return "Invalid PIN"
        if amount < 500:
            raise MinimValueError("Withdrawal amount must be at least 500")
        if amount > self._balance:
            raise MinimValueError("Insufficient balance")
        self._balance -= amount
        return f"Withdrawal successful! New balance: {self._balance}"

    def run(self):
        while True:
            print("\n===== ACCOUNT MENU =====")
            for key, value in self.menu.items():
                print(f"{key}. {value}")

            choice = input("Choose an option: ")

            try:
                if choice == "1":
                    amount = float(input("Enter deposit amount: "))
                    print(self.deposit(amount))

                elif choice == "2":
                    amount = float(input("Enter withdrawal amount: "))
                    pin = int(input("Enter PIN: "))
                    print(self.withdraw(amount, pin))

                elif choice == "3":
                    old_pin = int(input("Enter old PIN: "))
                    new_pin = int(input("Enter new PIN: "))
                    print(self.change_pin(old_pin, new_pin))

                elif choice == "4":
                    new_pin = int(input("Enter new PIN: "))
                    print(self.reset_pin(new_pin))

                elif choice == "5":
                    pin = int(input("Enter PIN to check balance: "))
                    print(self.check_balance(pin))

                elif choice == "6":
                    print("Exiting... Thank you!")
                    break

                else:
                    print("Invalid choice. Please try again.")

            except MinimValueError as e:
                print("Error:", e)
            except ValueError:
                print("Please enter valid numeric input.")
            except Exception as e:
                print("Unexpected error:", e)


if __name__ == "__main__":
    try:
        account = Account("John", "123456789", 1000, 1234)
        account.run()
    except MinimValueError as e:
        print(str(e))
