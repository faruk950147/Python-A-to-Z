class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(self.id, self.name, self.salary)

class Company:
    def __init__(self, name):
        self.name = name
        # Accessing Employee class inside Company class
        self.employee = Employee(123, "John", 5000)

    def display(self):
        print(self.name)
        # Accessing Employee class inside Company class
        self.employee.display() 
if __name__ == "__main__":        
    # Creating Company class object
    company = Company("ABC")
    company.display()