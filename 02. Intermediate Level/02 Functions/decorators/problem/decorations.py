# string formatting decorators

def string_upper_case(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper

@string_upper_case
def print_name(name):
    return name

print(print_name("faruk"))