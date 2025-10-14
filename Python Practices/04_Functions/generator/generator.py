# ============================= What is Generator =============================
# A generator is a function that returns an iterator.

# ============================= Generator Function =============================

from re import sub


def generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# ============================= Generator Object =============================
generator_object = generator()
print(generator_object)
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))

def gen(num):
    for i in range(num):
        yield i

generator_object = gen(10)
print(generator_object)
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))

# ============================= Generator Expression =============================
generator_expression = (i for i in range(10))
print(generator_expression)
print(next(generator_expression))
print(next(generator_expression))
print(next(generator_expression))
print(next(generator_expression))
print(next(generator_expression))
print(next(generator_expression))
print(next(generator_expression))
print(next(generator_expression))
print(next(generator_expression))
print(next(generator_expression))


# ============================= Generator vs List =============================
list_ = [i for i in range(10)]
print(list_)
print(next(list_))
print(next(list_))
print(next(list_))
print(next(list_))
print(next(list_))
print(next(list_))
print(next(list_))
print(next(list_))
print(next(list_))
print(next(list_))


# ============================= Generator sum =============================

def gen_sum(num):
    for i in range(num):
        yield i

print(sum(gen_sum(10)))

def gen_sub(num):
    for i in range(num):
        yield -i
print(sum(gen_sub(10)))