# comments in python
# comments are lines of code that are not executed by the interpreter
# comments are used to make the code more readable
# comments are used to explain the code
# comments are used to debug the code
# comments are used to disable a piece of code

# single line comment
# this is a single line comment

# multi line comment
"""
this is a multi line comment
"""
class Car:
    def __init__(self, make, model):
        # single line comment
        # self is an instance of the class
        # make and model are attributes of the class
        # self is a reference to the current object
        # make and model are parameters
        # this is a constructor it is called when an object is created
        self.make = make
        self.model = model

    def __str__(self):
        """
        this is a string representation of the object it is called when the object is printed
        f string is used to format the string
        {self.make} and {self.model} are placeholders for the values of the attributes
        return is used to return the value of the function
        f"{self.make} {self.model}" is a formatted string
        """
        return f"{self.make} {self.model}"