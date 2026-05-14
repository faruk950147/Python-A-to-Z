# def swap_case(s):
#     return s.swapcase()

# print(swap_case("Hello World"))


# def swap_case(s):
#     result = ""
#     for char in s:
#         if char.isupper():
#             result += char.lower()
#         elif char.islower():
#             result += char.upper()
#         else:
#             result += char
#     return result

# print(swap_case("Hello World"))



def swap_case(s):
    chars = []
    for char in s:
        if char.islower():
            chars.append(char.upper())
        elif char.isupper():
            chars.append(char.lower())
        else:
            chars.append(char)
    return ''.join(chars)

print(swap_case("Hello World"))
