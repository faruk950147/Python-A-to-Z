# ============================ What is Programming & What is Python ============================

# Programming:
# Programming is the process of giving instructions to a computer to perform specific tasks.
# These instructions are written using programming languages.

# Example:
print("Hello, World!")
# This code tells the computer to display “Hello, World!” on the screen.


# Python:
# Python is a High-Level, Interpreted, Object-Oriented Programming Language.
# It was created by Guido van Rossum in 1991.
# Python is popular for its simple and easy-to-read syntax.
# It is widely used in Web Development, Data Science, Machine Learning,
# Artificial Intelligence, and Automation.


# ============================ Implicit Datatype Language ============================

# Definition:
# A programming language where the variable datatype does not need to be declared explicitly.
# The language automatically determines the datatype based on the assigned value.
# Such a language is called an Implicit Datatype Language.

# Example Languages: Python, JavaScript, PHP


# Example in Python:
a = 10          # Python automatically detects this as an integer (int)
b = 3.14        # Automatically detected as a float
c = "Faruk"     # Automatically detected as a string
d = True        # Automatically detected as a boolean

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Output:
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>

# Explanation:
# In Python, we don’t need to declare the datatype.
# The interpreter automatically determines it.
# Therefore, Python is an Implicit Datatype Language.


# ============================ Explicit Datatype Language ============================

# Definition:
# A programming language where the datatype of a variable must be declared explicitly
# before assigning a value is called an Explicit Datatype Language.

# Example Languages: C, C++, Java


# Example in C:

#include <stdio.h>
# int main() {
#     int a = 10;          // integer
#     float b = 3.14;      // float
#     char c[] = "Faruk";  // string
#     int d = 1;           // used as boolean

#     printf("a = %d\n", a);
#     printf("b = %.2f\n", b);
#     printf("c = %s\n", c);
#     printf("d = %d\n", d);

#     return 0;
# }
# */

# Output:
# a = 10
# b = 3.14
# c = Faruk
# d = 1

# Explanation:
# Here, the datatype of each variable is declared explicitly (int, float, char).
# Therefore, C is an Explicit Datatype Language.


# ============================ Comparison (Implicit vs Explicit) ============================

# | Feature                | Implicit Datatype Language       | Explicit Datatype Language       |
# |------------------------|----------------------------------|----------------------------------|
# | Datatype Declaration   | Automatically determined         | Manually declared by programmer  |
# | Example Languages      | Python, JavaScript, PHP          | C, C++, Java                     |
# | Example Code           | x = 10                           | int x = 10;                      |
# | Type System            | Dynamically Typed                | Statically Typed                 |
# | Error Detection        | Found at runtime                 | Found at compile time            |


# ============================ Conclusion ============================

# Python is an Implicit Datatype Language
# C / C++ / Java are Explicit Datatype Languages

# That means, in Python you don’t need to declare the datatype,
# but in C you must declare it, otherwise it will cause an error.
