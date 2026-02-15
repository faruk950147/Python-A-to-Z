# itertools is a module in python that provides various functions 
# that work on iterators to produce complex iterators

# ===============================
# Python itertools Cheat Sheet
# ===============================
from itertools import *
import operator

print("1. count(start=0, step=1):")
for i in count(5, 2):
    print(i, end=' ')
    if i > 10: break
print("\n")

print("2. cycle(iterable):")
c = 0
for x in cycle(['A','B','C']):
    print(x, end=' ')
    c += 1
    if c == 6: break
print("\n")

print("3. repeat(object, times=None):")
print(list(repeat(10,3)))
print("\n")

print("4. product(*iterables, repeat=1):")
print(list(product([1,2], ['x','y'])))
print(list(product([0,1], repeat=3)))
print("\n")

print("5. permutations(iterable, r=None):")
print(list(permutations([1,2,3],2)))
print("\n")

print("6. combinations(iterable, r):")
print(list(combinations([1,2,3],2)))
print("\n")

print("7. combinations_with_replacement(iterable, r):")
print(list(combinations_with_replacement([1,2],2)))
print("\n")

print("8. chain(*iterables):")
for x in chain([1,2],['a','b']): print(x, end=' ')
print("\n")

print("9. compress(data, selectors):")
print(list(compress(['A','B','C'], [1,0,1])))
print("\n")

print("10. filterfalse(function, iterable):")
print(list(filterfalse(lambda x:x%2==0, [1,2,3,4])))
print("\n")

print("11. accumulate(iterable, func=operator.add):")
print(list(accumulate([1,2,3,4])))
print(list(accumulate([1,2,3,4], operator.mul)))
print("\n")

print("12. groupby(iterable, key=None):")
for k,g in groupby([1,1,2,2,3,3]):
    print(k, list(g))
print("\n")

print("13. islice(iterable, start, stop, step):")
print(list(islice(range(10),2,8,2)))
print("\n")

print("14. starmap(function, iterable):")
print(list(starmap(pow, [(2,3),(4,5)])))
print("\n")

print("15. tee(iterable, n=2):")
it1,it2 = tee([1,2,3],2)
print(list(it1))
print(list(it2))
