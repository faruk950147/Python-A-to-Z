from functools import wraps

# Global user state (simple simulation)
user = {
    "is_logged_in": False
}


# Login required decorator
def is_logged_in_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not user["is_logged_in"]:
            print("Login required")
            return
        return func(*args, **kwargs)
    return wrapper


# Logout required decorator
def is_logged_out_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if user["is_logged_in"]:
            print("Logout required")
            return
        return func(*args, **kwargs)
    return wrapper


# Login function
@is_logged_out_required
def login():
    user["is_logged_in"] = True
    print("Logged in successfully")


# Logout function
@is_logged_in_required
def logout():
    user["is_logged_in"] = False
    print("Logged out successfully")


# -------------------------
# TEST RUN (IMPORTANT PART)
# -------------------------

login()   # should login
login()   # should block
logout()  # should logout
logout()  # should block