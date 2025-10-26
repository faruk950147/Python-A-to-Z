
x = 10  # global variable

def func():
    global x  # tells Python to use the global x
    x = 20    # modifies global x
    print("Inside function, global x changed to 20:", x)
    print("Globals dictionary:", globals())

    local_x = 30  # this is a local variable, not global
    print("Inside function, local variable local_x:", local_x)
    print("Globals dictionary after local variable:", globals())

func()

print("Outside function, global x:", x)
print("All global variables:", globals())


# =============================== modifying global scope ===============================
x = 10

def func():
    global x   # allow access and modification of the global x
    x = 20
    print("Inside function (global x changed to 20):", x)
    print(globals()['x'])  # access the global x using globals()

func()

# Outside the function, we can change the value of global x using globals()
globals()['x'] = 200
print("Outside function (global x changed to 200):", x)
