def isPalindrome(word):
    word = word.lower()
    word = ''.join(c for c in word if c.isalnum())
    return word == word[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))

def isPalindrome1(word):
    return word == word[::-1]

print(isPalindrome1("mam"))

def isPalindrome2(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(isPalindrome2("mam"))

def isPalindrome3(word):
    isPalindrome = True
    for i in range(len(word) // 2):
        # that's why we use -i - 1 because we want to compare the first and last character
        # i means first character and -i - 1 means last character
        # for example, if word is "mam", then i = 0 and -i - 1 = 2
        # so, word[i] = "m" and word[-i - 1] = "m"
        # if word is "mam", then i = 1 and -i - 1 = 1
        # so, word[i] = "a" and word[-i - 1] = "a"
        if word[i] != word[-i - 1]: 
            isPalindrome = False
            break
    return isPalindrome

print(isPalindrome3("mam"))