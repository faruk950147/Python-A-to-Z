# Login required decorator
def is_logged_in(func):
    def wrapper():
        # Check if user is logged in
        if not hasattr(wrapper, 'user'):
            print("Login required")
            return
        return func()
    return wrapper

# Logout required decorator
def is_logged_out(func):
    def wrapper():
        # Check if user is logged out
        if hasattr(wrapper, 'user'):
            print("Logout required")
            return
        return func()
    return wrapper

