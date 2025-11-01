import re

text = "+8801712345678"  #  +919876543210

# Bangladesh phone pattern
bd_pattern = r"^(\+?88)?01[3-9]\d{8}$"

# India phone pattern
in_pattern = r"^(\+?91)?[6-9]\d{10}$"
# r is for raw string
# ^ means start of the string
# (\+?88)? is for group
# \+ means + sign 1 or more | ? means optional  
# [3-9] means any character in the set that is 3 to 9
# \d{10} means any digit 10 times
# $ means end of the string

if re.match(bd_pattern, text):
    if text.startswith("+88"):
        print(f"Valid Bangladeshi phone (with +88): {text}")
    else:
        print(f"Valid Bangladeshi phone (without country code): {text}")

elif re.match(in_pattern, text):
    if text.startswith("+91"):
        print(f"Valid Indian phone (with +91): {text}")
    else:
        print(f"Valid Indian phone (without country code): {text}")

else:
    print("Invalid phone number")

