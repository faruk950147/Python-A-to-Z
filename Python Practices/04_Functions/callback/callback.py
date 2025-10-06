# ============================= What is callback function =============================
# A callback function is a function that is passed as an argument to another function and is executed inside that function.

# Example: callback function
def simple(a, b, callback):
    return callback(a, b)
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
print(simple(10, 20, add))
print(simple(10, 20, sub))
print(simple(10, 20, mul))
print(simple(10, 20, div))

# ============================= function as argument =======================================
# Example: passing a function into another function

def doTask(task, callback):
    print("Doing task:", task)
    callback() # calling the callback function

def done():
    print("Task finished!")

def notify():
    print("Sending notification...")

doTask("Learning JS", done)
doTask("Completing Homework", notify)

# ============================= function returning function ================================
# Example: a function that creates and returns another function

def createMultiplier(x):
    def multiplier(y):
        return x * y
    return multiplier

multiplyBy2 = createMultiplier(2)
print(multiplyBy2(5)) # Output: 10

# ============================= built-in higher-order functions ============================
from functools import reduce
# map(), filter(), reduce(), sorted(), any(), all()
# Example: map()
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers) # Output: [1, 4, 9, 16, 25]

# Example: filter()
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))
print(even_numbers) # Output: [2, 4]

# Example: reduce()
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
sum = reduce(add, numbers)  # noqa: F821
print(sum) # Output: 15

# Example: sorted()
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers) # Output: [1, 2, 5, 5, 6, 9]

# Example: any()
def is_positive(x):
    return x > 0

numbers = [1, 2, 3, 4, 5]
result = any(is_positive, numbers)
print(result) # Output: True

# Example: all()
def is_positive(x):
    return x > 0

numbers = [1, 2, 3, 4, 5]
result = all(is_positive, numbers)
print(result) # Output: True
