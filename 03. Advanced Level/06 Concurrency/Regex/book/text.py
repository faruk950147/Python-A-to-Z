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

import re
# =============================== re.findall ===============================
# re.findall() returns all matches
text = "Bangladesh India New Zealand Netherlands Iceland"
match = re.findall(r"\w+land", text) 
if match:
    print(f"1. Found {match}")
else:
    print(f"1. Not found {text}")
# output: ['land', 'land', 'land', 'land']
# =============================== re.search ===============================

# re.search() returns the first match
text = "Bangladesh India New Zealand Netherlands Iceland"
match = re.search(r"\w+", text)
if match:
    print(f"2. Found {match.group()}")
else:
    print(f"2. Not found {text}")
# output: Bangladesh
# =============================== re.match ===============================

# re.match() returns the match at the start of the string
text = "Bangladesh India New Zealand Netherlands Iceland"
match = re.match(r"\w+", text)
if match:
    print(f"3. Found {match.group()}")
else:
    print(f"3. Not found {text}")
# output: Bangladesh
# =============================== \w ===============================

# \w matches any word character (alphanumeric & underscore)
text = "Bangladesh India New Zealand Netherlands Iceland"
match = re.search(r"\w+", text)
if match:
    print(f"4. \w Found {match.group()}")
else:
    print(f"4. \w Not found {text}")

# =============================== \d ===============================

text = "Bangladesh India New Zealand Netherlands Iceland"
match = re.search(r"\d+", text)
if match:
    print(f"5. \d Found {match.group()}")
else:
    print(f"5. \d Not found {text}")
# output: Not found Bangladesh India New Zealand Netherlands Iceland
# =============================== ^ ===============================

# caret (^) matches the start of the string
text = "Bangladesh India New Zealand Netherlands Iceland"
match = re.search(r"^\w+", text)
if match:
    print(f"4. ^ Found {match.group()}")
else:
    print(f"4. ^ Not found {text}")
# output: Bangladesh

# =============================== $ ===============================

# dollar sign ($) matches the end of the string
text = "Bangladesh India New Zealand Netherlands Iceland"
match = re.search(r"\w+$", text)
if match:
    print(f"5. $ Found {match.group()}")
else:
    print(f"5. $ Not found {text}")
# output: Iceland

# =============================== . ===============================

# dot (.) matches any single character
text = "Bangladesh India New Zealand Netherlands Iceland"
match = re.search(r".", text)
if match:
    print(f"6. . Found {match.group()}")
else:
    print(f"6. . Not found {text}")
# output: B

# =============================== * ===============================

# star (*) matches zero or more occurrences of the pattern
text = "Bangladesh India New Zealand Netherlands Iceland"
match = re.search(r"\w*", text)
if match:
    print(f"7. * Found {match.group()}")
else:
    print(f"7. * Not found {text}")
# output: Bangladesh
# =============================== + ===============================

# plus (+) matches one or more occurrences of the pattern
text = "Bangladesh India New Zealand Netherlands Iceland"
match = re.search(r"\w+", text)
if match:
    print(f"8. + Found {match.group()}")
else:
    print(f"8. + Not found {text}")
# output: Bangladesh    

