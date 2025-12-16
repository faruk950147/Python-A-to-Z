# print function syntax
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# objects = "Hello", "World"
# sep = " "
# end = "\n", "-", "!" " "
# file = "output.txt"
# flush means buffer free action and it is used to flush the buffer.

print("Hello", "World") # Output: Hello World
print("A", "B", "C", sep='-')   # Output: A-B-C
print("Hello", end=' ')  # Output: Hello 

f = open('output.txt', 'w')
print("Hello, File!", file=f, flush=True)
f.close()