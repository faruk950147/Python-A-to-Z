
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
        
