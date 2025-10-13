def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_10 = outer_function(10)

print(add_10(5))            # Output: 15
print(add_10.__closure__)   # Check closure info
print(add_10.__closure__[0].cell_contents) # Check closure value details