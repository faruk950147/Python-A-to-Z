
import re

# Country codes and names
country_codes = {
    '880': 'Bangladesh',
    '91': 'India',
    '1': 'USA / Canada',
    '44': 'United Kingdom',
    '61': 'Australia',
    '81': 'Japan',
    '49': 'Germany',
    '33': 'France',
    '39': 'Italy',
    '34': 'Spain',
    '86': 'China',
    '7': 'Russia',
}

# Regex pattern (international format)
pattern = re.compile(r'^\+?(\d{1,3})?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{4}$')

# Test number list
numbers = [
    "+8801712345678",
    "01712345678",
    "+919876543210",
    "+14155552671",
    "+447912345678",
    "+61412345678",
    "12345"
]

for num in numbers:
    match = pattern.match(num)
    if match:
        code = match.group(1)  # country code (if exists)
        if code in country_codes:
            print(f"{num} → {country_codes[code]}")
        elif code is None and num.startswith("01"):
            print(f"{num} → Bangladesh (local)")
        else:
            print(f"{num} → Unknown country (code: {code})")
    else:
        print(f"{num} → Invalid phone number")
