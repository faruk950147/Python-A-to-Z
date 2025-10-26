from datetime import datetime
from typing import List, Tuple, Optional

class ATM:
    def __init__(self, account_number: str, pin: str, initial_balance: float = 0.0,
                 daily_withdrawal_limit: float = 1000.0):
        self.account_number = account_number
        self._pin = pin
        self._balance = float(initial_balance)
        self.daily_withdrawal_limit = float(daily_withdrawal_limit)
        self._withdrawn_today = 0.0
        self._last_withdrawal_day = None  # yyyy-mm-dd string
        self._history: List[str] = []
        self._log(f"Account created. Initial balance: {self._balance:.2f}")
        
        self.menu = {
            
        }

    # --- internal helpers ---
    def _today_str(self) -> str:
        return datetime.utcnow().date().isoformat()

    def _reset_daily_if_needed(self):
        today = self._today_str()
        if self._last_withdrawal_day != today:
            self._withdrawn_today = 0.0
            self._last_withdrawal_day = today

    def _log(self, text: str):
        ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        self._history.append(f"{ts} — {text}")

    # --- public methods ---
    def verify_pin(self, pin: str) -> Tuple[bool, str]:
        """Return (True, 'OK') if pin matches, else (False, message)."""
        if pin == self._pin:
            return True, "PIN verified."
        return False, "Invalid PIN."

    def check_balance(self, pin: str) -> Tuple[bool, str]:
        ok, msg = self.verify_pin(pin)
        if not ok:
            return False, msg
        return True, f"Balance: {self._balance:.2f}"

    def deposit(self, amount: float, pin: str) -> Tuple[bool, str]:
        ok, msg = self.verify_pin(pin)
        if not ok:
            return False, msg
        if amount <= 0:
            return False, "Deposit amount must be positive."
        self._balance += float(amount)
        self._log(f"Deposit: +{amount:.2f} => balance {self._balance:.2f}")
        return True, f"Deposit successful. New balance: {self._balance:.2f}"

    def withdraw(self, amount: float, pin: str) -> Tuple[bool, str]:
        ok, msg = self.verify_pin(pin)
        if not ok:
            return False, msg
        if amount <= 0:
            return False, "Withdraw amount must be positive."
        self._reset_daily_if_needed()
        if self._withdrawn_today + amount > self.daily_withdrawal_limit:
            return False, (f"Daily withdrawal limit exceeded. "
                           f"Allowed remaining: {self.daily_withdrawal_limit - self._withdrawn_today:.2f}")
        if amount > self._balance:
            return False, "Insufficient funds."
        self._balance -= float(amount)
        self._withdrawn_today += float(amount)
        self._log(f"Withdraw: -{amount:.2f} => balance {self._balance:.2f}")
        return True, f"Withdraw successful. New balance: {self._balance:.2f}"

    def transfer(self, amount: float, to_atm: 'ATM', pin: str) -> Tuple[bool, str]:
        """Transfer amount from this account to another ATM instance (same process: pin, funds)."""
        ok, msg = self.verify_pin(pin)
        if not ok:
            return False, msg
        if not isinstance(to_atm, ATM):
            return False, "Destination account invalid."
        if amount <= 0:
            return False, "Transfer amount must be positive."
        if amount > self._balance:
            return False, "Insufficient funds."
        # Do transfer (no exceptions used; assume to_atm accepts deposit via internal method)
        self._balance -= float(amount)
        to_atm._balance += float(amount)
        self._log(f"Transfer out: -{amount:.2f} to {to_atm.account_number} => balance {self._balance:.2f}")
        to_atm._log(f"Transfer in: +{amount:.2f} from {self.account_number} => balance {to_atm._balance:.2f}")
        return True, f"Transfer successful. New balance: {self._balance:.2f}"

    def mini_statement(self, pin: str, lines: Optional[int] = 10) -> Tuple[bool, List[str]]:
        ok, msg = self.verify_pin(pin)
        if not ok:
            return False, [msg]
        return True, self._history[-lines:]

    # getters for testing or UI (no pin required)
    @property
    def balance(self) -> float:
        return self._balance

    @property
    def history(self) -> List[str]:
        return list(self._history)
