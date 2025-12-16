import time

# ============================= What is a Decorator ==============================
# A decorator is a function that takes another function as an argument,
# adds or modifies functionality, and returns a new function.
# It allows you to extend or modify the behavior of functions or methods
# without changing their code.



# ============================= Practical Use Cases ============================

# ---------- Authorization Example ----------
def require_admin(func):
    def wrapper(user):
        if user == "admin":
            return func(user)
        else:
            print("Access denied!")
    return wrapper

@require_admin
def view_dashboard(user):
    print(f"{user} is viewing the dashboard")

view_dashboard("admin")
view_dashboard("guest")


# ---------- Caching Example ----------
cache = {}
def cached(func):
    def wrapper(x):
        if x in cache:
            print("Returning from cache")
            return cache[x]
        print("Calculating...")
        result = func(x)
        cache[x] = result
        return result
    return wrapper

@cached
def square(n):
    return n * n

print(square(4))
print(square(4))


# ---------- Timing Example ----------
def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing
def slow_function():
    time.sleep(1)
    print("Done")

slow_function()
