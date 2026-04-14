
def remove_vowel(word):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in word:
        if ch not in vowels:
            result += ch
    return result

print(remove_vowel("Hello World"))
import re

def remove_vowel(word):
    return re.sub(r"[aeiouAEIOU]", "", word)
print(remove_vowel("Hello World"))


def remove_vowel(word):
    return word.translate(str.maketrans('', '', 'aeiouAEIOU'))

print(remove_vowel("Hello World"))
