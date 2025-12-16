# ============================== what is command line arguments ============================== #
# command line arguments are the arguments that are passed to the program when it is run.
# command line arguments are passed to the program as a list of strings.
# command line arguments are accessed using the sys module.
# command line arguments are accessed using the argv variable.
# argv is a list of strings where the first string is the name of the script and the rest are the arguments.
# Example
# syntax of argv is: argv = sys.argv
# print(argv)

# ============================== how to use command line arguments ============================== #
# command line arguments are passed to the program as a list of strings.
# command line arguments are accessed using the sys module.
# command line arguments are accessed using the argv variable.
# argv is a list of strings where the first string is the name of the script and the rest are the arguments.
# Example
# syntax of argv is: argv = sys.argv
# print(argv)

# ============================== how to run command line arguments ============================== #
# command line arguments are passed to the program as a list of strings.
# command line arguments are accessed using the sys module.
# command line arguments are accessed using the argv variable.
# argv is a list of strings where the first string is the name of the script and the rest are the arguments.
# Example
# syntax of argv is: argv = sys.argv
# print(argv)

# ============================== example ============================== #
# filename: calculator.py
import sys
lst = sys.argv
print(lst)
print(type(lst))
print(lst[0])
print(lst[1])
for i in lst:
    print(i)

# ============================== run ============================== #
# python main.py 10 20 4.5 'hello' 'world' (1, 2, 3, 4, 5)

# ============================== output ============================== #
# ['main.py', '10', '20', '4.5', 'hello', 'world']
