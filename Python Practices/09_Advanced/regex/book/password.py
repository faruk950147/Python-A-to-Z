import re

pattern = r"^[0-9a-zA-Z$@]{6,}$" # that means any string that starts with a and ends with s and has 3 characters in between

password = input("Enter a password: ")
match = re.findall(pattern, password)
if match:
    print("Password is valid")
else:
    print("Password is not valid")