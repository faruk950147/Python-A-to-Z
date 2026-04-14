
def update_string(string, index, char):
    return string[:index] + char + string[index + 1:]

print(update_string("hello", 1, "xl"))

# hello -> hxllo


