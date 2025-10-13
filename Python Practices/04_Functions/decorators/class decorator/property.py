class Student:
    def __init__(self, name, age, grade):
        # Initialize instance attributes
        self.name = name
        self.age = age
        self.grade = grade

    @property   # getter decorator allows only reading like an attribute
    def message(self):
        # Return a message string using name and grade
        # Acts like an attribute (not a method)
        return f"{self.name} got grade {self.grade}"

    @message.setter   # setter decorator allows only setting like an attribute
    def message(self, msg):
        # msg format: "Alice 22 A"
        # Split the string into parts
        parts = msg.split(" ")
        # Assign values to object attributes
        self.name = parts[0]
        self.age = int(parts[1])
        self.grade = parts[2]



if __name__ == "__main__":
    # Create a Student object
    student = Student("John", 20, "A+")

    # Property getter works (acts like reading an attribute)
    print(student.message)
    # Output: John got grade A+

    # Update grade → property value automatically updates
    student.grade = "B"
    print(student.message)
    # Output: John got grade B

    # Property setter works (acts like assigning an attribute)
    student.message = "Alice 22 A"

    # The attributes have now been updated
    print(student.name, student.age, student.grade)
    # Output: Alice 22 A

    # The property getter reflects the updated data
    print(student.message)
    # Output: Alice got grade A
