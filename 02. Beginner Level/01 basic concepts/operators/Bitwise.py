print(8 >> 1)   # 4 (8 divided by 2^1 = 4)
print(8 >> 2)   # 2 (8 divided by 2^2 = 2)
print(8 >> 3)   # 1 (8 divided by 2^3 = 1)

# Left shift examples
print(4 << 1)   # 8 (4 multiplied by 2^1 = 8)
print(4 << 2)   # 16 (4 multiplied by 2^2 = 16)
print(4 << 3)   # 32 (4 multiplied by 2^3 = 32)

# Bitwise AND examples
print(12 & 10)  # 8 (1100 & 1010 = 1000)
print(15 & 7)   # 7 (1111 & 0111 = 0111)

# Bitwise OR examples
print(12 | 10)  # 14 (1100 | 1010 = 1110)
print(15 | 7)   # 15 (1111 | 0111 = 1111)

# Bitwise XOR examples
print(12 ^ 10)  # 6 (1100 ^ 1010 = 0110)
print(15 ^ 7)   # 8 (1111 ^ 0111 = 1000)

# Bitwise NOT examples
print(~12)      # -13 (bitwise NOT of 12)
print(~10)      # -11 (bitwise NOT of 10)