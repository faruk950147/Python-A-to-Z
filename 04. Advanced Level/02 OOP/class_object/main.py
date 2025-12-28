class Card:
    def __init__(self, card_number, pin):
        self._card_number = card_number
        self._pin = pin

    def get_card_number(self):
        return self._card_number

    def verify_pin(self, entered_pin):
        return self._pin == entered_pin

class Account:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self._balance}")
            return amount
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient funds.")
            return 0

class Keypad:
    def get_input(self, prompt):
        return input(prompt)

class Screen:
    def display_message(self, message):
        print(message)

    def display_options(self, options):
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

class CashDispenser:
    def __init__(self, initial_cash):
        self._cash = initial_cash

    def dispense_cash(self, amount):
        if amount > 0 and amount <= self._cash:
            self._cash -= amount
            print(f"Dispensing ${amount}.")
            return True
        elif amount <= 0:
            print("Invalid amount to dispense.")
            return False
        else:
            print("Insufficient cash in ATM.")
            return False

    def get_remaining_cash(self):
        return self._cash

class ReceiptPrinter:
    def print_receipt(self, transaction_type, amount, balance):
        print("\n----- Receipt -----")
        print(f"Transaction Type: {transaction_type}")
        print(f"Amount: ${amount}")
        print(f"New Balance: ${balance}")
        print("-------------------\n")

class ATM:
    def __init__(self, bank_database, initial_cash):
        self._bank_database = bank_database
        self._cash_dispenser = CashDispenser(initial_cash)
        self._screen = Screen()
        self._keypad = Keypad()
        self._receipt_printer = ReceiptPrinter()
        self._current_card = None
        self._current_account = None
        self._is_authenticated = False

    def _authenticate_user(self):
        card_number = self._keypad.get_input("Enter your card number: ")
        entered_pin = self._keypad.get_input("Enter your PIN: ")

        self._current_card = self._bank_database.get_card(card_number)

        if self._current_card and self._current_card.verify_pin(entered_pin):
            self._current_account = self._bank_database.get_account(self._current_card.get_card_number())
            if self._current_account:
                self._is_authenticated = True
                self._screen.display_message("Authentication successful.")
                return True
            else:
                self._screen.display_message("Error: Account not found for this card.")
                return False
        else:
            self._screen.display_message("Authentication failed. Incorrect card number or PIN.")
            return False

    def _display_main_menu(self):
        self._screen.display_options(["View Balance", "Withdraw Cash", "Deposit Funds", "Exit"])

    def _get_user_choice(self):
        while True:
            choice = self._keypad.get_input("Enter your choice: ")
            if choice in ["1", "2", "3", "4"]:
                return choice
            else:
                self._screen.display_message("Invalid choice. Please try again.")

    def _view_balance(self):
        balance = self._current_account.get_balance()
        self._screen.display_message(f"Your current balance is: ${balance}")

    def _withdraw_cash(self):
        amount_str = self._keypad.get_input("Enter the amount to withdraw: $")
        try:
            amount = float(amount_str)
            if amount > 0:
                cash_dispensed = self._current_account.withdraw(amount)
                if cash_dispensed > 0 and self._cash_dispenser.dispense_cash(cash_dispensed):
                    self._receipt_printer.print_receipt("Withdrawal", cash_dispensed, self._current_account.get_balance())
                elif cash_dispensed > 0:
                    self._screen.display_message("Error: ATM has insufficient cash. Please try a smaller amount.")
                    # Revert the withdrawal from the account if ATM can't dispense
                    self._current_account.deposit(cash_dispensed)
            else:
                self._screen.display_message("Invalid withdrawal amount.")
        except ValueError:
            self._screen.display_message("Invalid input. Please enter a numeric amount.")

    def _deposit_funds(self):
        amount_str = self._keypad.get_input("Enter the amount to deposit: $")
        try:
            amount = float(amount_str)
            if amount > 0:
                self._current_account.deposit(amount)
                self._receipt_printer.print_receipt("Deposit", amount, self._current_account.get_balance())
            else:
                self._screen.display_message("Invalid deposit amount.")
        except ValueError:
            self._screen.display_message("Invalid input. Please enter a numeric amount.")

    def run(self):
        self._screen.display_message("Welcome to the ATM!")
        if self._authenticate_user():
            while True:
                self._display_main_menu()
                choice = self._get_user_choice()

                if choice == "1":
                    self._view_balance()
                elif choice == "2":
                    self._withdraw_cash()
                elif choice == "3":
                    self._deposit_funds()
                elif choice == "4":
                    self._screen.display_message("Thank you for using the ATM. Goodbye!")
                    break

        self._current_card = None
        self._current_account = None
        self._is_authenticated = False
        self._screen.display_message("Please take your card.")

class BankDatabase:
    def __init__(self):
        self._accounts = {
            "123456": Account("123456", 1000.50),
            "789012": Account("789012", 500.75),
            "345678": Account("345678", 2000.00)
        }
        self._cards = {
            "5555111122223333": Card("5555111122223333", "1234"),
            "9999888877776666": Card("9999888877776666", "5678"),
            "1111222233334444": Card("1111222233334444", "9012")
        }

    def get_account(self, card_number):
        account_number = self._get_account_number_from_card(card_number)
        return self._accounts.get(account_number)

    def get_card(self, card_number):
        return self._cards.get(card_number)

    def _get_account_number_from_card(self, card_number):
        # In a real system, this would involve a more complex lookup
        # Here, we'll just make a simple association for demonstration
        card_to_account = {
            "5555111122223333": "123456",
            "9999888877776666": "789012",
            "1111222233334444": "345678"
        }
        return card_to_account.get(card_number)

# --- Main Execution ---
if __name__ == "__main__":
    bank_database = BankDatabase()
    atm = ATM(bank_database, 5000)  # ATM starts with $5000 cash
    atm.run()