import re

country_codes = {
    '880': 'Bangladesh',
    '91': 'India',
}

pattern = re.compile(r'^\+?(\d{1,3})?(\d+)$')

numbers = [
    "+8801712345678",  # BD intl
    "01712345678",     # BD local
    "+919876543210",   # India intl
    "09876543210",     # India local
    "+99123456789",    # Unknown
    "12345"            # Invalid
]

for num in numbers:
    clean_num = re.sub(r'[\s\-.]', '', num)
    match = pattern.match(clean_num)

    if match:
        code = match.group(1)  # This will be None if no +country code
        main_number = match.group(2)

        # International known country
        if code in country_codes:
            print(f"{num} → {country_codes[code]} (international)")
        # Bangladesh local
        elif (code is None and clean_num.startswith("01") and len(clean_num) == 11) or clean_num.startswith("+880"):
            print(f"{num} → Bangladesh (local / +880)")
        # India local
        elif (code is None and clean_num.startswith("09") and len(clean_num) == 11) or clean_num.startswith("+91"):
            print(f"{num} → India (local / +91)")
        # Unknown international code
        elif code is not None and code not in country_codes:
            print(f"{num} → Unknown country (code: {code})")
        else:
            print(f"{num} → Invalid phone number")
    else:
        print(f"{num} → Invalid phone number")
