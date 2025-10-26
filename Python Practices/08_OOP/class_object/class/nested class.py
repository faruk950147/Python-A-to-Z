class University:
    def __init__(self, name):
        self.name = name
        # class of University current object
        self.department = self.Department("Department")
        
    def display(self):
        print(self.name)

    class Department:
        def __init__(self, name):
            self.name = name

        def display(self):
            print(self.name)
if __name__ == "__main__":
    u = University("TMSS Technical University")
    u.display()
    u.department.display()
    u.department1 = u.Department("CSE")
    u.department2 = u.Department("EEE")

    u.department1.display()  # CSE
    u.department2.display()  # EEE

