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
from functools import reduce

# map(), filter(), reduce(), sorted(), any(), all()
def square(x):
    return x * x

print(f"list(map(square, range(1, 6))): {list(map(square, range(1, 6)))}")

print(f"list(filter(lambda x: x % 2 == 0, range(1, 6))): {list(filter(lambda x: x % 2 == 0, range(1, 6)))}")

print(f"reduce(lambda x, y: x + y, range(1, 6)): {reduce(lambda x, y: x + y, range(1, 6))}")

print(f"sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]): {sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])}")

print(f"any([False, False, True]): {any([False, False, True])}")

print(f"all([True, True, True]): {all([True, True, True])}")

