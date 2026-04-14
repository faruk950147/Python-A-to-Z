def remove_space_0(word):
    # Base case: if the string is empty, return an empty string
    if len(word) == 0:
        return "is empty"
    # If the first character is a space, skip it and continue with the rest
    if word[0] == " ":
        return remove_space_0(word[1:])
    # Otherwise, keep the first character and continue with the rest
    return word[0] + remove_space_0(word[1:])

print(f"remove_space_0: {remove_space_0('')}")


'''
def remove_space_1(word):
    # Base case: if the string is empty, return an empty string
    if len(word) == 0:
        return ""
    # Otherwise, replace all spaces with empty string
    else:
        return word.replace(" ", "")

print(f"remove_space_1: {remove_space_1('Hello World')}")

def remove_space_2(word):
    # Base case: if the string is empty, return an empty string
    return word.replace(" ", "")

print(f"remove_space_2: {remove_space_2('Hello World')}")

'''
