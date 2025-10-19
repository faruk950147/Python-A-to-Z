def is_bd_phone(phone):
    # bd phone number
    # international format
    if phone.startswith("+880") and len(phone) == 13:
        return True
    # local format
    elif phone.startswith("01") and len(phone) == 11:
        return True
    # india phone number
    elif phone.startswith("+91") and len(phone) == 12:
        return True
    # uzbekistan phone number
    elif phone.startswith("+998") and len(phone) == 13:
        return True
    else:
        return False

# Example usage
print(is_bd_phone("+8801712345678"))  # True
print(is_bd_phone("01712345678"))     # True
print(is_bd_phone("+880912345678"))   # False
