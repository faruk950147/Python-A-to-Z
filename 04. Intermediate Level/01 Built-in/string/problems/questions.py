# input 'my23name45is'
# output 'si23eman45ym'
def reverseString(word):
    output = ''
    # Stack of letters (reversed)
    alpha = [char for char in reversed(word) if char.isalpha()]
    i = 0
    for char in word:
        if char.isalpha():
            output += alpha[i]
            i += 1
        else:
            output += char
    return output


print(reverseString('my23name45is'))

def reverseString(word):
    letters = [c for c in word if c.isalpha()]  # Stack of letters
    output = ''

    for c in word:
        if c.isalpha():
            output += letters.pop()  # Take letters from the end
        else:
            output += c  # Keep non-letters in place
    return output

print(reverseString('my23name45is'))


# word = 'my23name45is'
# output = ''
# alpha = [char for char in reversed(word) if char.isalpha()]
# print(alpha)
# i = 0
# for char in word:
#     if char.isalpha():
#         output += alpha[i]
#         i += 1
#     else:
#         output += char
# print(output)