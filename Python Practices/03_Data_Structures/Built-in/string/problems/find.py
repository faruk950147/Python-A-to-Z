# find() and rfind()
# find() returns the index of the first occurrence of the value
# rfind() returns the index of the last occurrence of the value

def find_str(word, find):
    return word.find(find)

print(find_str("you", "you"))


def r_find_str(word, find):
    return word.rfind(find)

print(r_find_str("you", "you"))

def find_str2(word, find):
    return word.index(find)

print(find_str2("you", "you"))
