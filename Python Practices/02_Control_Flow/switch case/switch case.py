# Sure! In Python 3.10+, you can use the match-case statement, which is the modern way to do switch-case. It works very similarly to C/Java switch-case.

# Example:

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")


# Output:

# Wednesday


# Notes:

# case _: is like the default in C/Java — it runs if no other case matches.

# You can also match multiple values in one case:

match day:
    case 1 | 2:
        print("Start of the week")
    case 3:
        print("Middle of the week")
    case _:
        print("Other day")


# This is cleaner and more readable than long if-elif-else chains.