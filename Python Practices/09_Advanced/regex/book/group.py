# Group is a set of characters that you want to match.
# It is denoted by ()

import re

pattern = r"(abc|def)"
text = "abc def ghi jkl"
match = re.findall(pattern, text)
print(match)
