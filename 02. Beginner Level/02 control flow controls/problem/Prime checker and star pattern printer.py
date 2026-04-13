# def is_prime(n):
#     """Check if a number is prime"""
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1): # n**0.5 thats means square root 25**0.5 = 5
#         if n % i == 0:
#             return False
#     return True
# # --- Program Run ---
# num = int(input("Enter a number to check if it's prime: "))

# if is_prime(num):
#     print(f"{num} is a Prime Number.")
# else:
#     print(f"{num} is NOT a Prime Number.")


def pyramid(rows):
    """Pyramid Pattern"""
    print("\nPyramid Pattern\n")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)


def inverted_pyramid(rows):
    """Inverted Pyramid Pattern"""
    print("\nInverted Pyramid Pattern\n")
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "* " * i)


def diamond(rows):
    """Diamond Pattern"""
    print("\nDiamond Pattern\n")
    # Upper part
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)
    # Lower part
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "* " * i)


# --- Program Run ---
rows = int(input("\nEnter number of rows for pattern: "))

pyramid(rows)
inverted_pyramid(rows)
diamond(rows)
