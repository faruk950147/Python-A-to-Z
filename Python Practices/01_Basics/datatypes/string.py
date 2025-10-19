# =================== String ===================
# string type is a sequence type it has only one `value
# string → a sequence of characters
single_quoted = 'Hello' # it can be used with single quotes
double_quoted = "Hello" # it can be used with double quotes
triple_quoted = """Hello""" # it can be used with triple quotes

print(type(single_quoted)) # <class 'str'>
print(type(double_quoted)) # <class 'str'>
print(type(triple_quoted)) # <class 'str'>

# ==================== string length ===================
print(len(single_quoted)) # 5
print(len(double_quoted)) # 5
print(len(triple_quoted)) # 5

# ==================== string indexing positive ===================
print(single_quoted[0]) # H
print(single_quoted[1]) # e
print(single_quoted[2]) # l
print(single_quoted[3]) # l
print(single_quoted[4]) # o

# ==================== string indexing negative ===================
print(single_quoted[-1]) # o
print(single_quoted[-2]) # l
print(single_quoted[-3]) # l
print(single_quoted[-4]) # e
print(single_quoted[-5]) # H

# ==================== substring ===================
substring = single_quoted[0:2]
print(substring) # He

substring = single_quoted[0:1]
print(substring) # H

substring = single_quoted[1:2]
print(substring) # e

substring = single_quoted[2:3]
print(substring) # l

substring = single_quoted[3:4]
print(substring) # l

substring = single_quoted[4:5]
print(substring) # o


