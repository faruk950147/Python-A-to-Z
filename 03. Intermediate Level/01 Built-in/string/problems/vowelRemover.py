
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


'''
maketrans() creates a translation table that maps each character to be replaced 
to its replacement character. 
str.maketrans() returns a mapping table that can be used 
with the translate() method to replace specified characters.

translate() method returns a string where some specified characters are replaced 
with the character described in a dictionary, or in a mapping table.
'''

def remove_vowel(word):
    return word.translate(str.maketrans('', '', 'aeiouAEIOU'))

print(remove_vowel("Hello World"))
