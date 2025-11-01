import re

# Regex pattern (international format)
pattern = re.compile(r'^\+?(\d{1,3})?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{4}$')

text = input("Enter a phone number: ")

match = re.match(pattern, text)

if match and text.startswith("88"):
    print("Valid Bangladeshi phone number")
elif match and text.startswith("91"):
    print("Valid Indian phone number")
else:
    print("Invalid phone number")
