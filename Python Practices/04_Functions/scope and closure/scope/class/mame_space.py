# =============== Class Space =================
class Test:
    def __init__(self):
        self.num = 10

    def display(self):
        print(f"Class Scope: {dir(self)}")

# =============== Global Space =================
print(f"Global Scope: {dir()}")
test = Test()
test.display()
print(f"Global Scope: {dir()}")