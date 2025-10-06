def remove_vowel(word):
    vowels = "aeiouAEIOU"
    for i in range(len(word)):
        if word[i] in vowels:
            word = word.replace(word[i], "")
    return word
    