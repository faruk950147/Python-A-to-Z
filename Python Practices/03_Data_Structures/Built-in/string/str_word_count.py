def str_word_count(string):
    return len(string.split())

print(str_word_count("Hello World"))

def str_word_count1(string):
    count = 0
    for i in string:
        if i == " ":
            count += 1
    return count + 1

print(str_word_count1("Hello World"))

def str_word_count2(string):
    count = 0
    for i in range(len(string)):
        if string[i] == " ":
            count += 1
    return count + 1
print(str_word_count2("Hello World"))