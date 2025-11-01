# Character class is a set of characters that you want to match.
# It is denoted by [ ]

import re

pattern = r"[0-9]" # that means any number
text = "abc def ghi jkl 123"
match = re.findall(pattern, text)
print(match)

pattern = r"[a-z]" # that means any alphabet
text = "abc def ghi jkl 123"
match = re.findall(pattern, text)
print(match)

pattern = r"[A-Z]" # that means any alphabet in uppercase
text = "ABC def ghi jkl 123"
match = re.findall(pattern, text)
print(match)

pattern = r"[a-zA-Z0-9]" # that means any alphabet or number in any case
text = "abc def ghi jkl 123"
match = re.findall(pattern, text)
print(match)


