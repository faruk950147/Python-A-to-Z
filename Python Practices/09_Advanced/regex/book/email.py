import re

# [a-zA-Z0-9._%+-]+: One or more characters that can be letters, numbers, dots, underscores, percent signs, plus signs, or hyphens.
# @: The @ symbol.
# [a-zA-Z0-9.-]+: One or more characters that can be letters, numbers, dots, or hyphens.
# \.: The dot character (escaped with a backslash because it has a special meaning in regular expressions).
# [a-zA-Z]{2,}: Two or more letters.

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
text = "faruk950147@gmail.com"

if re.fullmatch(pattern, text):
    print("Valid email address")
else:
    print("Invalid email address")
