# ============================= iterators =============================
# Iterator is an object that can be iterated (looped) upon.
# It is a way to create an iterator by using the iterator protocol.
# It is a way to create an iterator by using the iterator protocol.

# 1. Example
list = [1, 2, 3, 4, 5]
iterator = iter(list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# 2. Example
for i in list:
    print(i)

# 3. Example
for i in range(5):
    print(i)

# 4. Example
for i in "Hello":
    print(i)

# 5. Example
for i in (1, 2, 3, 4, 5):
    print(i)

# 6. Example
for i in {1, 2, 3, 4, 5}:
    print(i)

# 7. Example
for i in {"a", "b", "c", "d", "e"}:
    print(i)

# 8. Example
for i in {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}:
    print(i)

# 9. Example
for i in {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}.values():
    print(i)

# 10. Example
for i in {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}.keys():
    print(i)

# 11. Example
for i in {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}.items():
    print(i)

# 12. Example
for i in {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}.keys():
    print(i)

# 13. Example
for i in {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}.values():
    print(i)

# ============================= generators =============================
# Generator is an iterator that is created by a generator function.
# It is a way to create a generator by using the generator protocol.

# 1. Example
def generator_function():
    yield 1
    yield 2
    yield 3

for i in generator_function():
    print(i)

# 2. Example
def generator_function(n):
    for i in range(n):
        yield i

for i in generator_function(5):
    print(i)

