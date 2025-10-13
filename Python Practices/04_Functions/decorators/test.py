def decorator(func, word):
    func(word)

def display(word):
    print("Hello", word)

decorator(display, "World")