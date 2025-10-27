# Static method is a method that is bound to the class, not the instance (object).
# It cannot access or modify the class or instance state.
# It is marked using the @staticmethod decorator.
# Example below is NOT using a static method — it’s showing how instance and class variables differ.

# 1. Instance method: Change the name of the college through an object instance.
# But this will NOT change the class variable — it will only create a new instance variable.

# class Person:
#      # Class variable (shared by all objects)
#     college_name = "TMSS Technical Institute"

#     def changeName(self, collage_name):
#         # Here 'self' refers to the instance, not the class.
#         # So this line creates a NEW instance variable named 'college_name'
#         # instead of changing the class variable.
#         self.college_name = collage_name


# if __name__ == "__main__":
#     p1 = Person()
#     p1.changeName("TTI")   # Changes only for p1, not for the class

#     print(p1.college_name)       # Output: TTI (instance variable)
#     print(Person.college_name)   # Output: TMSS Technical Institute (class variable remains unchanged)

# 2. Class method: Change the name of the college through the class.
# This will change the class variable for ALL objects.

# class Person2:
#     name = "John"

#     def changeName(self, name):
#         Person2.name = name   # here class variable name is changed or modified it is changed name of class variable

# if __name__ == "__main__":
#     p1 = Person2()
#     p1.changeName("Doe")

#     print(p1.name)        # Output: Doe
#     print(Person2.name)   # Output: Doe

# 3. Class method: Change the name of the college through the class.
# This will change the class variable for ALL objects.
class Person3:
    name = "John"

    @classmethod
    def changeName(cls, name):
        cls.name = name

if __name__ == "__main__":
    p1 = Person3()
    p1.changeName("Doe")

    print(p1.name)        # Output: Doe
    print(Person3.name)   # Output: Doe
