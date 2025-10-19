def rev_str(word):
    rev_string = ''
    for char in word:
        rev_string = char + rev_string   # every time new char add in front
    return rev_string

print(rev_str("you"))

def rev_str2(word):
    return word[::-1]

print(rev_str2("you"))