import sys

with open(sys.argv[1], "w") as f:
    f.write(sys.argv[2])
    
with open(sys.argv[1], "r") as f:
    print(f.read())


import sys

if len(sys.argv) < 3:
    print("Usage: python script.py <filename> <text>")
    sys.exit(1)

with open(sys.argv[1], "w") as f:
    f.write(sys.argv[2])

with open(sys.argv[1], "r") as f:
    print(f.read())

# python file.py filename.txt "Hello World"