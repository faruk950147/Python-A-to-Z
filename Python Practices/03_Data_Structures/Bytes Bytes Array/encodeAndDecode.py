# Pure Python string
str1 = "Hello World"
# print(f"Pure Python string: {str1}")
# print(f"Type of Pure Python string: {type(str1)}")

# string to bytes
str2 = str1.encode(encoding="utf-8") # encoding="utf-8" is default it's optional argument
str2 = str1.encode() # encoding="utf-8" is default it's optional argument
# print(f"String to bytes: {str2}")
# print(f"Type of String to convert bytes: {type(str2)}")

# bytes to string
str3 = str2.decode(encoding="utf-8") # encoding="utf-8" is default it's optional argument
str3 = str2.decode() # encoding="utf-8" is default it's optional argument
print(f"Bytes to string: {str3}")
print(f"Type of Bytes to convert string: {type(str3)}")
