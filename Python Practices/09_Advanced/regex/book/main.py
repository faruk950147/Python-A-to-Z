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

# 1. Example
import re
# =============================== re.findall ===============================
# re.findall () takes two arguments: the pattern and the string.
# It returns a list of all non-overlapping matches of pattern in string, as a list of strings.
pattern = r'(\w+land *)'
string = "Bangladesh America Afghanistan Cambodia China Denmark New York New Lands Netherlands"
# re.IGNORECASE ignores case sensitivity. and it is optional.flag
matches = re.findall(pattern, string, re.IGNORECASE)
print(matches)

# =============================== re.search ===============================
# re.search () takes two arguments: the pattern and the string.
# It returns a match object if the pattern is found in the string, otherwise it returns None.

pattern = r"(\w+a*)"
string = "Bangladesh America Afghanistan Cambodia China Denmark"

# 1. method
# re.IGNORECASE ignores case sensitivity. and it is optional.flag
if re.search(pattern, string, re.IGNORECASE):
    print("Match found!")
else:
    print("Match not found!")
    
# 2. method
# re.IGNORECASE ignores case sensitivity. and it is optional.flag
match = re.search(pattern, string, re.IGNORECASE)
if match:
    print(match.group()) # group () returns the part of the string where there is a match.
else:
    print("Match not found!")
    
    
# =============================== re.match ===============================
# re.match () takes two arguments: the pattern and the string.
# It returns a match object if the pattern is found at the start of the string, otherwise it returns None.

pattern = r"America"
string = "America Bangladesh"

# 1. method
# re.IGNORECASE ignores case sensitivity. and it is optional.flag
if re.match(pattern, string, re.IGNORECASE):
    print("Match found!")
else:
    print("Match not found!")
    
# 2. method
# re.IGNORECASE ignores case sensitivity. and it is optional.flag
match = re.match(pattern, string, re.IGNORECASE)
if match:
    print(match.group()) # group () returns the part of the string where there is a match.
else:
    print("Match not found!")
    