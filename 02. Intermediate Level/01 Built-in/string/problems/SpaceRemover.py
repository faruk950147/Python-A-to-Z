def remove_space0(word):
    if len(word) == 0:
        return ""
    if word[0] == " ":
        return remove_space0(word[1:])
    return word[0] + remove_space0(word[1:])

print(f"remove_space0: {remove_space0('Hello World')}")

def remove_space1(word):
    if len(word) == 0:
        return ""
    else:
        return word.replace(" ", "")

print(f"remove_space1: {remove_space1('Hello World')}")

def remove_space(word):
    return word.replace(" ", "")

print(f"remove_space: {remove_space('Hello World')}")


