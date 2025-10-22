# Pure Python string
str1 = "Hello World"
# print(f"Pure Python string: {str1}")
# print(f"Type of Pure Python string: {type(str1)}")

# string to bytes
str2 = str1.encode()
# print(f"String to bytes: {str2}")
# print(f"Type of String to convert bytes: {type(str2)}")

# bytes to string
str3 = str2.decode()
print(f"Bytes to string: {str3}")
print(f"Type of Bytes to convert string: {type(str3)}")
