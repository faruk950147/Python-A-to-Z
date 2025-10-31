import re

# ====================== . dot any character ======================
string = "Bangladesh"
match = re.search("..", string)
if match:
    print(match.group())
else:
    print("Not found")

match = re.search("B.n", string)
if match:
    print(match.group())
else:
    print("Not found")
if match:
    print(match.group())
else:
    print("Not found")
if match:
    print(match.group())
else:
    print("Not found")

# ====================== ^ character start ======================
string = "Bangladesh"
match = re.search("^B", string)
if match:
    print(match.group())
else:
    print("Not found")

# ====================== $ character end ======================
string = "Bangladesh"
match = re.search("d$", string)
if match:
    print(match.group())
else:
    print("Not found")

# ====================== * character 0 or more ======================
string = "Bangladesh"
match = re.search("B.*d", string)
if match:
    print(match.group())
else:
    print("Not found")
    
# ====================== + character 1 or more ======================
string = "Bangladesh"
match = re.search("B.+d", string)
if match:
    print(match.group())
else:
    print("Not found")
    
# ====================== ? character 0 or 1 ======================
string = "Bangladesh"
match = re.search("B.+d", string)
if match:
    print(match.group())
else:
    print("Not found")
    

# ====================== {n} character n times ======================
string = "Bangladesh"
match = re.search("B.{3}d", string)
if match:
    print(match.group())
else:
    print("Not found")
    
    
# ====================== \w word ======================
string = "Bangladesh"
match = re.search("\w", string)
if match:
    print(match.group())
else:
    print("Not found")
    
# ====================== \W not word ======================
string = "Bangladesh"
match = re.search("\W", string)
if match:
    print(match.group())
else:
    print("Not found")
