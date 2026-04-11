import re

class Managers:
    def __init__(self):
        pass

    def normalize_phone(self, phone):
        phone = re.sub(r"\s+", "", phone)

        if phone.startswith("+880"):
            return phone
        if phone.startswith("880"):
            return "+" + phone
        if phone.startswith("01"):
            return "+880" + phone[1:]

        return phone


# object
m = Managers()

# method call 
result = m.normalize_phone("01712345678")

print(result)