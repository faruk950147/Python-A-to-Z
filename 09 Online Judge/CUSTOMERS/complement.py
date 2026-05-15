# efficient solution
def FindComplement(num):
    # first get num bit length
    bit_length = num.bit_length()
    
    # right now get mask using bit_length
    mask = (1 << bit_length) - 1
    
    # right now get complement using bitwise XOR
    return num ^ mask

print(FindComplement(5))  # Output: 2

# less efficient solution or pythonic way
def FindComplement2(num):
    binary = bin(num)[2:]  # convert binary string  ('0b' remove)
    
    # using list comprehension complement create
    complement = ''.join('1' if b == '0' else '0' for b in binary)
    
    # complement binary string to integer
    return int(complement, 2)


# Example
print(FindComplement2(5))   # Output: 2
print(FindComplement2(1))   # Output: 0
print(FindComplement2(10))  # Output: 5

# bad solution
def FindComplement3(num):
    binary = bin(num)[2:]
    complement = ''  # empty string
    
    for b in binary:
        if b == '0':
            complement += '1'
        else:
            complement += '0'
    
    return int(complement, 2)
