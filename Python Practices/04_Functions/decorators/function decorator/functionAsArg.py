# ============================= Function as an argument =========================

def decorator1(func):
    func()

def display1():
    print("Hello World!")

decorator1(display1)
# ============================= Function as an argument =========================
def decorator2(func, word):
    func(word)

def display2(word):
    print("Hello", word + "!")

decorator2(display2, "World")

