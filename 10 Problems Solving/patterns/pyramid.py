
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
