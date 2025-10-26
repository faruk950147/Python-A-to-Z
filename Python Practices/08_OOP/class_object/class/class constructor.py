# ========================= what is class constructor =========================
# class constructor is a special method that is called when an object is created
# it is defined using __init__()
# its main purpose is to initialize object attributes

# ========================= types of class constructor =====================
# 1. Default constructor
# 2. Parameterized constructor
# 3. Non-Parameterized constructor


# ========================= Example 1: Default Constructor =====================
class DefaultConstructor:
    def __init__(self):
        self.name = "Default User"
        self.age = 0

    def showInfo(self):
        print(f"[Default Constructor] Name: {self.name}, Age: {self.age}")


# ========================= Example 2: Parameterized Constructor =====================
class ParameterizedConstructor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print(f"[Parameterized Constructor] Name: {self.name}, Age: {self.age}")


# ========================= Example 3: Non-Parameterized Constructor =====================
class NonParameterizedConstructor:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))

    def showInfo(self):
        print(f"[Non-Parameterized Constructor] Name: {self.name}, Age: {self.age}")


# ========================= Object Creation and Output =========================

# 1. Default Constructor Object
default_obj = DefaultConstructor()
default_obj.showInfo()

# 2. Parameterized Constructor Object
param_obj = ParameterizedConstructor("Faruk Ahmed", 22)
param_obj.showInfo()

# 3. Non-Parameterized Constructor Object
non_param_obj = NonParameterizedConstructor()
non_param_obj.showInfo()
