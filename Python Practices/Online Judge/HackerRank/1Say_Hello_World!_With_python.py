# my_string = "Hello, World!"
# print(my_string)

def person_lister(format_func):
    # decorator function and inner function is used to sort the people list by age
    def inner(people): # get people list 4 parameter firstname, lastname, age, gender
        # age wise sorted list of people
        # sorted is a built-in function that returns a new sorted list from the elements of any sequence
        # get two parameter from people list 1
        # this people is a list of tuples and sorted function sort the list of tuples by age
        # key=lambda person: int(person[2]) is a lambda function that returns the age of a person
        # people is a list
        # key is a function that returns a value to be used for sorting
        # and iterable is a list of tuples 
        sorted_people = sorted(people, key=lambda person: int(person[2]))
        # sorted_people list age wise sorted tuples
        return [format_func(person) for person in sorted_people]
    return inner

@person_lister
def format_name(person):
    # format name function and inner function is used to sort the people list by age
    title = "Mr. " if person[3] == "M" else "Ms. "
    full_name = f"{person[0]} {person[1]}"
    return title + full_name

if __name__ == '__main__':
    try:
        n = int(input("Enter number of people: "))
        # n number of people input
        people = [input("Enter first name, last name, age, gender: ").split() for _ in range(n)]
        # people list of tuples
        # people = [('John', 'Doe', '25', 'M'), ('Jane', 'Smith', '22', 'F'), ...]
        print(*format_name(people), sep='\n')
    except ValueError:
        print("Please enter a valid integer.")
# input
# 3
# Mike Thomson 20 M
# Robert Bustle 32 M
# Julia Kumar 40 F
# output
# Mr. Mike Thomson
# Ms. Julia Kumar
# Mr. Robert Bustle







