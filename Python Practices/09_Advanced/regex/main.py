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
# =============================== re.findall ===============================
# re.findall () takes two arguments: the pattern and the string.
# It returns a list of all non-overlapping matches of pattern in string, as a list of strings.
pattern = r'(\w+land *)'
string = "Bangladesh America Afghanistan Cambodia China Denmark New York New Lands Netherlands"
matches = re.findall(pattern, string)
print(matches)

# =============================== re.search ===============================
# re.search () takes two arguments: the pattern and the string.
# It returns a match object if the pattern is found in the string, otherwise it returns None.
pattern = r"(\w+a*)"
string = "Bangladesh America Afghanistan Cambodia China Denmark"
if re.search(pattern, string):
    print("Match found!")
else:
    print("Match not found!")
match = re.search(pattern, string)
if match:
    print(match.group()) # group () returns the part of the string where there is a match.
else:
    print("Match not found!")
    
    
# =============================== re.match ===============================
# re.match () takes two arguments: the pattern and the string.
# It returns a match object if the pattern is found at the start of the string, otherwise it returns None.

pattern = r"America"
string = "America Bangladesh"
if re.match(pattern, string):
    print("Match found!")
else:
    print("Match not found!")
match = re.match(pattern, string)
if match:
    print(match.group()) # group () returns the part of the string where there is a match.
else:
    print("Match not found!")
    
# =============================== re.sub ===============================
# re.sub () takes three arguments: the pattern, the replacement, and the string.
# It returns a new string with all occurrences of the pattern replaced by the replacement.
pattern = r"America"
string = "America Bangladesh"
new_string = re.sub(pattern, "America", string)
print(new_string)

# =============================== re.subn ===============================
# re.subn () takes three arguments: the pattern, the replacement, and the string.
# It returns a tuple containing the new string and the number of substitutions made.
pattern = r"America"
string = "America Bangladesh"
new_string, count = re.subn(pattern, "America", string)
print(new_string)
print(count)

# =============================== re.split ===============================
# re.split () takes two arguments: the pattern and the string.
# It returns a list of the string split by the pattern.
pattern = r"America"
string = "America Bangladesh"
split_list = re.split(pattern, string)
print(split_list)

