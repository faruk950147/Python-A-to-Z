# ============================= What is Iterator =============================
# An iterator is an object that implements the iterator protocol, 
# which consists of the __iter__() and __next__() methods.

# Example: iterator
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# ============================= Iterator Protocol =============================
# The iterator protocol is a set of methods that define how an object can be iterated over.
# The iterator protocol is implemented by the __iter__() and __next__() methods.