# what is continuation character in python?
# continuation character in python is a backslash (\). 

# Example


str1 = "Hello\
World"
a = 2 + 3 + 4 + 5 + \
    6 + 7 + 8 + 9 + 10 \
    + 11 + 12 + 13 + 14 + 15
print(a)

# another example
b = (3 * 4) + (5 * 6) + \
    (7 * 8) + (9 * 10) + \
    (11 * 12) + (13 * 14) + \
    (15 * 16)
print(b)

# another example
str1 = "Hello, World!"
str2 = "Hello, " + \
    "World!"
print(str1 == str2)