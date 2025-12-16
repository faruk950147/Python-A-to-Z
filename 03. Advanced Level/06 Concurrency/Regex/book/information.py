import re

# ========================== find all digit return list ==========================
pattern = r"\d"
text = "1235"
match = re.findall(pattern, text)
print(match)
# output: ['1', '2', '3', '5']

# ========================== find all digit return list  ==========================
pattern = r"\d+"
text = "1235"
match = re.findall(pattern, text)
print(match)
# output: ['1235']

# ========================== find all digit return list ==========================
pattern = r"\d*"
text = "1235"
match = re.findall(pattern, text)
print(match)
# output: ['1235', '']

# ========================== find all digit return list ==========================
pattern = r"\d?"
text = "1235"
match = re.findall(pattern, text)
print(match)
# output: ['1', '2', '3', '5', '']

# ========================== find all digit return list ==========================
pattern = r"\d{2}"
text = "1235"
match = re.findall(pattern, text)
print(match)
# output: ['12', '35']


