def remove_space_0(word):
    if len(word) == 0:
        return ""
    if word[0] == " ":
        return remove_space_0(word[1:])
    return word[0] + remove_space_0(word[1:])

print(f"remove_space_0: {remove_space_0(' H e l l o   W o r l d ')}")


'''
def remove_space_1(word):
    if len(word) == 0:
        return ""
    else:
        return word.replace(" ", "")

print(f"remove_space_1: {remove_space_1('Hello World')}")

def remove_space_2(word):
    return word.replace(" ", "")

print(f"remove_space_2: {remove_space_2('Hello World')}")

'''
