import re
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
# \w matches any word character (alphanumeric & underscore).
# \d matches any digit (0-9).
# \s matches any whitespace character.
# \S matches any non-whitespace character.
# square brackets ([]) matches any character within the brackets.
# round brackets () groups the pattern.
# curly braces ({} matches a specific number of occurrences of the pattern.)

phone = "phone number : 08801712345678"
if re.search(r'\d+', phone):
    print(re.search(r'\d+', phone).group())
else:
    print("Not found")

