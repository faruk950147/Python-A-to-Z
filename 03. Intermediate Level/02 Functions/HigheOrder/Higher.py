"""
============================= What is Higher-Order Function ==============================
A higher-order function is a function that:
- Takes one or more functions as arguments
- OR returns another function as a result

callback function is a function that is passed as an argument
to another function and is executed inside that function.

Callback Function

Callback function হলো এমন একটি function,
যেটাকে argument হিসেবে অন্য একটি function-এর মধ্যে পাঠানো হয়
এবং ওই function-এর ভিতরেই call (execute) করা হয়।

সহজ ভাষায়
একটি function আরেকটি function-কে বলে দেয়—
"আমার কাজ শেষ হলে তুমি এই functionটা চালাবে।"


Higher Order Function

Higher Order Function হলো এমন একটি function,
যেটা অন্য একটি function-কে argument হিসেবে নেয়
অথবা একটি function return করে।

সহজ ভাষায়
যে function, function নিয়ে কাজ করে
সেটাই Higher Order Function।


Callback Function vs Higher Order Function

| Callback Function                         | Higher Order Function                          |
| ----------------------------------------- | ---------------------------------------------- |
| যেই function-কে argument হিসেবে পাঠানো হয় | যেই function argument হিসেবে অন্য function নেয় |
| পাঠানো function                           | নেওয়া function                                 |
| Higher Order function-এর ভিতরে চলে        | Callback function-কে call করে                  |
| Example: add()                            | Example: calculate()                           |

simple() হলো Higher Order Function
কারণ:

এটা অন্য একটি function (callback) কে argument হিসেবে নিচ্ছে

তারপর সেই function-কে call করছে
add, sub, mul, div — এগুলো সবই Callback Function
কারণ:

এগুলোকে simple() function-এর মধ্যে argument হিসেবে পাঠানো হয়েছে

simple() এর ভিতরে এগুলো call (execute) হচ্ছে 
"""

# ============================= 1. Function as Argument =======================================

# def display(func):
#     print(func(2,3))
    
# def add(x, y):
#     return x + y

# def mul(x, y):
#     return x * y

# display(add)
# display(mul)

# ============================= 2. Function as Return =======================================
def display():
    def add(x, y):
        return x + y
    return add

add = display()
print(add(2, 3))


# ============================= 3. Function Higher Order =======================================

def display(func, nums):
    return func(nums)

def add(nums):
    return sum(nums)

add = display(add, [2, 3, 4])
print(add)
