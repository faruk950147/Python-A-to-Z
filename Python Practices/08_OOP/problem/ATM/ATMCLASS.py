from datetime import datetime
from typing import List, Dict, Union

class ATM:
    """A simple simulation of an ATM account with basic banking functionalities."""
    
    def __init__(self, account_number: str, pin: str, balance: float = 0.0,
                 daily_debit_limit: float = 1000.0, daily_credit_limit: float = 1000.0):
        self.account_number = account_number
        self._pin = pin
        self._balance = float(balance)
        # withdrawal limit
        self.daily_debit_limit = float(daily_debit_limit)
        self._debit_today = 0.0
        self._last_debit_day: Union[str, None] = None  # yyyy-mm-dd string
        # deposit limit
        self.daily_credit_limit = float(daily_credit_limit)
        self._credit_today = 0.0
        self._last_credit_day: Union[str, None] = None  # yyyy-mm-dd string
        
        # FIX: Changed self._history from Dict to List to support 'append'
        self._history: List[str] = [] 
        
        self._log(f"Account created. Initial balance: {self._balance:.2f}")
        
        self.menu = {
            "1": "Create Account", # Note: Already created in __init__ for this simulation
            "2": "Change Pin", 
            "3": "Reset Pin",      
            "4": "Debit (Withdrawal)",
            "5": "Credit (Deposit)",
            "6": "Check Balance",
            "7": "Transfer",
            "8": "Mini Statement",
            "9": "Exit"
        }
        print("Congratulations! Account created successfully.")
    
    # --- internal helpers ---
    def _today_str(self) -> str:
        """Returns the current date in ISO format (YYYY-MM-DD)."""
        return datetime.now().date().isoformat()
        
    def _reset_daily_if_needed(self):
        """Resets daily debit/credit counters if the last transaction was on a different day."""
        today = self._today_str()
        
        # Debit limit reset
        if self._last_debit_day != today:
            print(f"DEBUG: Debit daily limit of ${self.daily_debit_limit:.2f} reset.")
            self._debit_today = 0.0
            self._last_debit_day = today
            
        # FIX: Added Credit limit reset
        if self._last_credit_day != today:
            print(f"DEBUG: Credit daily limit of ${self.daily_credit_limit:.2f} reset.")
            self._credit_today = 0.0
            self._last_credit_day = today

    # FIX: Corrected _log to use list append
    def _log(self, text: str):
        """Logs a transaction or event with a timestamp."""
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        self._history.append(f"{ts} — {text}")
        
    def _authenticate(self) -> bool:
        """Prompts the user for a PIN and authenticates."""
        pin_entered = input("Enter your PIN to proceed: ")
        if pin_entered == self._pin:
            return True
        else:
            print("Invalid PIN.")
            return False

    # --- ATM operations ---

    def create_account(self):
        """Dummy function for the menu option."""
        print("\nNOTE: This account is already created. Please exit and restart to simulate a new account creation.")
        
    def change_pin(self):
        """Dummy function for the menu option."""
        print("\nNOTE: Pin change logic is not implemented in this simulation.")
        
    def reset_pin(self):
        """Dummy function for the menu option."""
        print("\nNOTE: Pin reset logic is not implemented in this simulation.")
        
    def debit(self):
        """Handles a cash withdrawal transaction."""
        print("\n--- 💸 Debit (Withdrawal) ---")
        if not self._authenticate():
            return

        self._reset_daily_if_needed()
        
        try:
            amount = float(input("Enter amount to withdraw: $"))
        except ValueError:
            print("Invalid amount entered.")
            return

        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self._balance:
            print(f"❌ Insufficient balance. Current balance: ${self._balance:.2f}")
        elif amount > (self.daily_debit_limit - self._debit_today):
            remaining = self.daily_debit_limit - self._debit_today
            print(f"❌ Daily debit limit of ${self.daily_debit_limit:.2f} exceeded.")
            print(f"You can only withdraw up to ${remaining:.2f} today.")
        else:
            self._balance -= amount
            self._debit_today += amount
            self._log(f"Debited ${amount:.2f}. New balance: ${self._balance:.2f}. Daily debit total: ${self._debit_today:.2f}")
            print(f"✅ Transaction successful. Please take your cash. Remaining balance: ${self._balance:.2f}")

    def credit(self):
        """Handles a cash deposit transaction."""
        print("\n---Credit (Deposit) ---")
        if not self._authenticate():
            return

        self._reset_daily_if_needed()
        
        try:
            amount = float(input("Enter amount to deposit: $"))
        except ValueError:
            print("Invalid amount entered.")
            return

        if amount <= 0:
            print("Deposit amount must be positive.")
        elif amount > (self.daily_credit_limit - self._credit_today):
            remaining = self.daily_credit_limit - self._credit_today
            print(f"Daily credit limit of ${self.daily_credit_limit:.2f} exceeded.")
            print(f"You can only deposit up to ${remaining:.2f} today.")
        else:
            self._balance += amount
            self._credit_today += amount
            # Update last credit day
            self._last_credit_day = self._today_str() 
            self._log(f"Credited ${amount:.2f}. New balance: ${self._balance:.2f}. Daily credit total: ${self._credit_today:.2f}")
            print(f"Deposit successful. New balance: ${self._balance:.2f}")
        
    def check_balance(self):
        """Displays the current account balance."""
        print("\n---Check Balance ---")
        if self._authenticate():
            print(f"Your current balance is: ${self._balance:.2f}")
        
    def transfer(self):
        """Dummy function for the menu option."""
        print("\nNOTE: Transfer logic is not implemented in this simulation.")
        
    def mini_statement(self):
        """Displays the last few transactions."""
        print("\n--- Mini Statement ---")
        if self._authenticate():
            if not self._history:
                print("No transactions to show.")
                return

            print("Recent Transactions:")
            # Display last 5 transactions
            for entry in self._history[-5:]:
                print(f"  {entry}")

    def run(self):
        """Runs the main ATM menu loop."""
        while True:
            print("\nATM Menu:")
            for key, value in self.menu.items():
                print(f"{key}: {value}")
                
            choice = input("Choose an option: ")
            
            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.change_pin()
            elif choice == "3":
                self.reset_pin()
            elif choice == "4":
                self.debit()
            elif choice == "5":
                self.credit()
            elif choice == "6":
                self.check_balance()
            elif choice == "7":
                self.transfer()
            elif choice == "8":
                self.mini_statement()
            elif choice == "9":
                print("\nGoodbye! Thank you for using the ATM. ")
                break
            else:
                print("Invalid choice. Please try again.")
                    
if __name__ == "__main__":
    # Example usage: create an ATM account with an initial balance of $500
    atm = ATM("1234567890", "1234", balance=500.0)
    atm.run()