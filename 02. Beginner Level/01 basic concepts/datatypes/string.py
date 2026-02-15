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
print(len(single_quoted)) # 5 (length of the string)
print(len(double_quoted)) # 5 (length of the string)
print(len(triple_quoted)) # 5 (length of the string)

# ==================== string indexing positive ===================
print(single_quoted[0]) # H (first character)
print(single_quoted[1]) # e (second character)
print(single_quoted[2]) # l (third character)
print(single_quoted[3]) # l (fourth character)
print(single_quoted[4]) # o (fifth character)

# ==================== string indexing negative ===================
print(single_quoted[-1]) # o (last character)
print(single_quoted[-2]) # l (second last character)
print(single_quoted[-3]) # l (third last character)
print(single_quoted[-4]) # e (fourth last character)
print(single_quoted[-5]) # H (fifth last character)

# ==================== substring ===================
# H   e   l   l   o
# 0   1   2   3   4

substring = single_quoted[0:2]
print(substring) # He (from index 0 to 2, excluding index 2)

substring = single_quoted[0:1]
print(substring) # H (from index 0 to 1, excluding index 1)

substring = single_quoted[1:2]
print(substring) # e (from index 1 to 2, excluding index 2)

substring = single_quoted[2:3]
print(substring) # l (from index 2 to 3, excluding index 3)

substring = single_quoted[3:4]
print(substring) # l (from index 3 to 4, excluding index 4)

substring = single_quoted[4:5]
print(substring) # o (from index 4 to 5, excluding index 5)
print(substring) # o


