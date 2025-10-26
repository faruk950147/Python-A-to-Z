# ============================= what is __init__ =============================
# __init__ is a magic method in Python that is called when an object is created.
# It is also known as a constructor.
# It is used to initialize the attributes of the object. 
# It is called automatically when an object is created.
# It is also known as a constructor.
# __init__.py is a special file in Python that is used to initialize the package.
# It is used to initialize the attributes of the package.
# It is called automatically when a package is imported.
# It is also known as a constructor.

class Person:
    def __init__(self):
        print("Person object created constructor")
if __name__ == "__main__":
    p = Person()