def count_bit(bit):
    return bin(bit).count('1')

print(count_bit(5)) # Output: 2 because 5 in binary is 101
print(count_bit(10)) # Output: 2 because 10 in binary is 1010
print(count_bit(100)) # Output: 3 because 100 in binary is 1100100