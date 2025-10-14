# ============================= What is callback function =============================
# callback function is a function that is passed as an argument
# to another function and is executed inside that function.

from functools import reduce
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
print(simple(10, 20, add)) # output: 30
print(simple(10, 20, sub)) # output: -10
print(simple(10, 20, mul)) # output: 200
print(simple(10, 20, div)) # output: 0.5

# ============================= function as argument =======================================
# Example: passing a function into another function

def doTask(task, callback):
    print("Doing task:", task)
    # calling the callback function
    callback() 


def done():
    print("Task finished!")

def notify():
    print("Sending notification...")

doTask("Learning JS", done) # output: Doing task: Learning JS
                            #         Task finished!
doTask("Completing Homework", notify) # output: Doing task: Completing Homework
                                        #         Sending notification...

def doTask(task, callback):
    print("Doing task:", task)
    # here callback function is done and " " + task + " done successfully!" is the argument 
    callback("Completed " + task + " done successfully!")  

def done(message):
    print("Task finished!", message)

def notify(message):
    print("Notification:", message)

doTask("Learning JS", done) # output: Doing task: Learning JS
                            #         Task finished! Completed Learning JS done successfully!
doTask("Completing Homework", notify) # output: Doing task: Completing Homework
                                        #         Notification: Completed Completing Homework done successfully!

def createMultiplier(x):
    def multiplier(y):
        return x * y
    return multiplier

multiplyBy2 = createMultiplier(2)
print(multiplyBy2(5)) # output: 10

# ============================= built-in higher-order functions ============================
# map(), filter(), reduce(), sorted(), any(), all()
# Example: map()
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers) # output: [1, 4, 9, 16, 25]

# Example: filter()
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))
print(even_numbers) # output: [2, 4]

# Example: reduce()
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
sum = reduce(add, numbers)  # noqa: F821
print(sum) # output: 15

# Example: sorted()
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers) # output: [1, 2, 5, 5, 6, 9]

# Example: any()
def is_positive(x):
    return x > 0

numbers = [1, 2, 3, 4, 5]
result = any(map(is_positive, numbers))
print(result) # output: True

# Example: all()
def is_positive(x):
    return x > 0

numbers = [1, 2, 3, 4, 5]
result = all(map(is_positive, numbers))
print(result) # output: True
