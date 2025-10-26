
from datetime import datetime
from typing import Dict

class ATM:
    def __init__(self, account_number: str, pin: str, balance: float = 0.0,
                 daily_debit_limit: float = 1000.0, daily_credit_limit: float = 1000.0):
        self.account_number = account_number
        self._pin = pin
        self._balance = float(balance)
        # withdrawal limit
        self.daily_debit_limit = float(daily_debit_limit)
        self._debit_today = 0.0
        self._last_debit_day = None  # yyyy-mm-dd string
        # deposit limit
        self.daily_credit_limit = float(daily_credit_limit)
        self._credit_today = 0.0
        self._last_credit_day = None  # yyyy-mm-dd string
        self._history: Dict[str, str] = {}
        self._log(f"Account created. Initial balance: {self._balance:.2f}")
        
        self.menu = {
            "1": "Create Account",
            "2": "Change Pin", 
            "3": "Reset Pin",      
            "4": "Debit",
            "5": "Credit",
            "6": "Check Balance",
            "7": "Transfer",
            "8": "Mini Statement",
            "9": "Exit"
        }
        print("Congratulations! Account created successfully.")
    
     # --- internal helpers ---
    def _today_str(self) -> str:
        return datetime.now().date().isoformat()
        
    def _reset_daily_if_needed(self):
        today = self._today_str()
        if self._last_debit_day != today:
            self._debit_today = 0.0
            self._last_debit_day = today

    def _log(self, text: str):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        self._history.append(f"{ts} — {text}")
        
    def create_account(self):
        print("Create Account")
        
    def change_pin(self):
        print("Change Pin")
        
    def reset_pin(self):
        print("Reset Pin")
        
    def debit(self):
        print("Debit")
        
    def credit(self):
        print("Credit")
        
    def check_balance(self):
        print("Check Balance")
        
    def transfer(self):
        print("Transfer")
        
    def mini_statement(self):
        print("Mini Statement")
        
    def run(self):
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
                break
            else:
                print("Invalid choice. Please try again.")
                    
if __name__ == "__main__":
    atm = ATM("1234567890", "1234")
    atm.run()