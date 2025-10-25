# ======================= what is return statement =======================
# return statement is used to return a value from a function
# return statement is used to exit a function
# return statement is used to end a function
# return statement is used to stop a function

# ======================= example of print statement =======================
def simple_interest(p, r, t):
    total = (p * r * t) / 100
    print("Simple Interest = ", total)

print(simple_interest(100, 10, 1))



# ======================= example of return statement =======================
# return by default returns None
# return can return any type of data
# return can return multiple values

def simple_interest(p, r, t):
    return (p * r * t) / 100

print(simple_interest(100, 10, 1))
