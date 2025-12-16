# String Methods
# capitalize(), casefold(), center(), count(), encode(), 
# endswith(), expandtabs(), find(), format(), format_map(), 
# index(), isalnum(), isalpha(), isascii(), isdecimal(), 
# isdigit(), isidentifier(), islower(), isnumeric(), isprintable(), 
# isspace(), istitle(), isupper(), join(), ljust(), lower(),
# lstrip(), maketrans(), partition(), removeprefix(), removesuffix(), 
# replace(), rfind(), rindex(), rjust(), rpartition(), rsplit(), rstrip(), 
# split(), splitlines(),startswith(), strip(), swapcase(), title(), translate(), upper(), zfill()

# 1. capitalize()
str = "hello world"
print(str.capitalize()) # capitalize() method returns a string where the first character is upper case
# output: Hello world

# 2. casefold()
str = "Hello World"
print(str.casefold()) # casefold() method returns a string where all the characters are lower case
# output: hello world

# 3. center()
str = "Hello World"
print(str.center(20)) # center() method returns a string where the specified value is centered in a string of the specified length
# output: Hello World

# 4. count()
str = "Hello World"
print(str.count("o")) # count() method returns the number of times a specified value appears in the string
# output: 2

# 5. encode()
str = "Hello World"
print(str.encode()) # encode() method returns an encoded version of the string
# output: b'Hello World'

# 6. endswith()
str = "Hello World"
print(str.endswith("World")) # endswith() method returns True if the string ends with the specified value
# output: True

str = "Hello World"
print(str.startswith("World", 0, 5)) # startswith() method returns True if the string starts with the specified value
# output: True

# 8. expandtabs()
str = "Hello\tWorld"
print(str.expandtabs(2)) # expandtabs() method returns a string where the specified value is replaced with the specified number of spaces
# output: Hello World

# 9. find()
str = "Hello World"
print(str.find("World")) # find() method returns the index of the specified value
# output: 6

str = "Hello World"
print(str.find("World", 0, 5)) # find() method returns the index of the specified value
# output: -1

# 10. format()
str = "Hello World"
print(str.format()) # format() method returns a formatted version of the string
# output: Hello World

# 11. format_map()
str = "Hello World"
print(str.format_map({"World": "Python"})) # format_map() method returns a formatted version of the string
# output: Hello Python

# 12. index()
str = "Hello World"
print(str.index("World")) # index() method returns the index of the specified value
# output: 6

str = "Hello World"
print(str.index("World", 0)) # index() method returns the index of the specified value
# output: 6

# 13. isalnum()
str = "Hello World"
print(str.isalnum()) # isalnum() method returns True if all characters in the string are alphanumeric
# output: False

str = "HelloWorld"
print(str.isalnum()) # isalnum() method returns True if all characters in the string are alphanumeric
# output: True

# 14. isalpha()
str = "Hello World"
print(str.isalpha()) # isalpha() method returns True if all characters in the string are alphabets
# output: False

str = "HelloWorld"
print(str.isalpha()) # isalpha() method returns True if all characters in the string are alphabets
# output: True

# 15. isascii()
str = "Hello World"
print(str.isascii()) # isascii() method returns True if all characters in the string are ascii characters
# output: True

str = "HelloWorld"
print(str.isascii()) # isascii() method returns True if all characters in the string are ascii characters
# output: True

# 16. isdecimal()
str = "Hello World"
print(str.isdecimal()) # isdecimal() method returns True if all characters in the string are decimal characters
# output: False

str = "HelloWorld"
print(str.isdecimal()) # isdecimal() method returns True if all characters in the string are decimal characters
# output: True

# 17. isdigit()
str = "Hello World"
print(str.isdigit()) # isdigit() method returns True if all characters in the string are digits
# output: False

str = "HelloWorld"
print(str.isdigit()) # isdigit() method returns True if all characters in the string are digits
# output: True

# 18. isidentifier()
str = "Hello World"
print(str.isidentifier()) # isidentifier() method returns True if the string is a valid identifier
# output: False

# 19. islower()
str = "Hello World"
print(str.islower()) # islower() method returns True if all characters in the string are lower case
# output: False

str = "HelloWorld"
print(str.islower()) # islower() method returns True if all characters in the string are lower case
# output: True

# 20. isnumeric()
str = "Hello World"
print(str.isnumeric()) # isnumeric() method returns True if all characters in the string are numeric
# output: False

str = "HelloWorld"
print(str.isnumeric()) # isnumeric() method returns True if all characters in the string are numeric
# output: True

# 21. isprintable()
str = "Hello World"
print(str.isprintable()) # isprintable() method returns True if all characters in the string are printable
# output: True

# 22. isspace()
str = "Hello World"
print(str.isspace()) # isspace() method returns True if all characters in the string are spaces
# output: False

str = "\t\n\r"
print(str.isspace()) # isspace() method returns True if all characters in the string are spaces
# output: True

# 23. istitle()
str = "Hello World"
print(str.istitle()) # istitle() method returns True if all characters in the string are title case
# output: False

str = "HelloWorld"
print(str.istitle()) # istitle() method returns True if all characters in the string are title case
# output: True

# 24. isupper()
str = "Hello World"
print(str.isupper()) # isupper() method returns True if all characters in the string are upper case
# output: False

str = "HelloWorld"
print(str.isupper()) # isupper() method returns True if all characters in the string are upper case
# output: True

# 25. join()
str = "Hello World"
print(str.join("Python")) # join() method returns a string where the specified value is joined by the specified separator
# output: PythonHello World

# 26. ljust()
str = "Hello World"
print(str.ljust(20)) # ljust() method returns a string where the specified value is left-justified in a string of the specified length
# output: Hello World

# 27. lower()
str = "Hello World"
print(str.lower()) # lower() method returns a string where all the characters are lower case
# output: hello world

# 28. lstrip()
str = "Hello World"
print(str.lstrip()) # lstrip() method returns a string where the specified value is left-stripped
# output: Hello World

# 29. maketrans()
str = "Hello World"
print(str.maketrans()) # maketrans() method returns a translation table
# output: Hello World

# 30. partition()
str = "Hello World"
print(str.partition("World")) # partition() method returns a tuple where the string is partitioned into three parts
# output: ('Hello', 'World', '')

# 31. removeprefix()
str = "Hello World"
print(str.removeprefix("Hello")) # removeprefix() method returns a string where the specified value is removed from the start of the string
# output: World

# 32. removesuffix()
str = "Hello World"
print(str.removesuffix("World")) # removesuffix() method returns a string where the specified value is removed from the end of the string
# output: Hello

# 33. replace()
str = "Hello World"
print(str.replace("World", "Python")) # replace() method returns a string where the specified value is replaced with the specified value
# output: Hello Python

# 34. rfind()
str = "Hello World"
print(str.rfind("World")) # rfind() method returns the index of the specified value
# output: 6

# 35. rindex()
str = "Hello World"
print(str.rindex("World")) # rindex() method returns the index of the specified value
# output: 6

# 36. rjust()
str = "Hello World"
print(str.rjust(20)) # rjust() method returns a string where the specified value is right-justified in a string of the specified length
# output: Hello World

# 37. rpartition()
str = "Hello World"
print(str.rpartition("World")) # rpartition() method returns a tuple where the string is partitioned into three parts
# output: ('Hello', 'World', '')

# 38. rsplit()
str = "Hello World"
print(str.rsplit("World")) # rsplit() method returns a list where the string is split into parts
# output: ['Hello', 'World']

# 39. rstrip()
str = "Hello World"
print(str.rstrip()) # rstrip() method returns a string where the specified value is right-stripped
# output: Hello World

# 40. split()
str = "Hello World"
print(str.split("World")) # split() method returns a list where the string is split into parts
# output: ['Hello', 'World']

# 41. splitlines()
str = "Hello World"
print(str.splitlines()) # splitlines() method returns a list where the string is split into lines
# output: ['Hello', 'World']

# 42. startswith()
str = "Hello World"
print(str.startswith("Hello")) # startswith() method returns True if the string starts with the specified value
# output: True

# 43. strip()
str = "Hello World"
print(str.strip()) # strip() method returns a string where the specified value is stripped
# output: Hello World

# 44. swapcase()
str = "Hello World"
print(str.swapcase()) # swapcase() method returns a string where the specified value is swapped
# output: Hello World

# 45. title()
str = "Hello World"
print(str.title()) # title() method returns a string where the specified value is title-cased
# output: Hello World

# 46. translate()
str = "Hello World"
print(str.translate()) # translate() method returns a string where the specified value is translated
# output: Hello World

# 47. upper()
str = "Hello World"
print(str.upper()) # upper() method returns a string where the specified value is upper-cased
# output: Hello World

# 48. zfill()
str = "Hello World"
print(str.zfill()) # zfill() method returns a string where the specified value is zero-filled
# output: Hello World



