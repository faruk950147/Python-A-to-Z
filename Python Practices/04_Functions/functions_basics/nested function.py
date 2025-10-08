# ============================= What is nested function ==============================

def outer():
    print("outer")
    def inner():
        print("inner")
    return inner

outer()