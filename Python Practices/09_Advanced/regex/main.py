# ============================= regex =============================
# Regular Expression (RegEx) is a sequence of characters that forms a search pattern.
# It is a way to match a string against a pattern.
# dot (.) matches any single character.
# caret (^) matches the start of the string.
# dollar sign ($) matches the end of the string.
# star (*) matches zero or more occurrences of the pattern.
# plus (+) matches one or more occurrences of the pattern.
# question mark (?) matches zero or one occurrence of the pattern.
# pipe (|) matches either the pattern before or the pattern after it.
# square brackets ([]) matches any character within the brackets.
# round brackets () groups the pattern.
# curly braces ({} matches a specific number of occurrences of the pattern.)

# 1. Example
import re
pattern = r"hello"
string = "hello world"
if re.search(pattern, string):
    print("Match found!")
else:
    print("Match not found!")

# 2. Example
pattern = r"hello"
string = "hello world"
matches = re.findall(pattern, string)
print(matches)

