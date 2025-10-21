# ================= what is iterator =================

# An iterator is an object that implements the iterator protocol, which consists of the __iter__() and __next__() methods.

# The __iter__() method returns the iterator object itself, and the __next__() method returns the next value in the sequence.

# When there are no more values to return, the __next__() method raises the StopIteration exception.

# Iterators are used in for loops, list comprehensions, and other places where a sequence of values is needed.

# ================= what is generator =================

# A generator is a function that returns an iterator.

# Generators are used to create iterators.

# Generators are used to create iterators.
dict1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
for item in dict1:
    print(f"{item} ======> {dict1[item]}")
    
for key, item in dict1.items():
    print(f"Keys {key} ======> Values {item}")