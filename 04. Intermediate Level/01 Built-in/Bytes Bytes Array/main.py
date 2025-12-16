# ===================== what is bytes ==========================
# bytes is an immutable sequence of bytes. 
# all elements of bytes must be in range(0, 256).
# used for representing binary data. also used for representing image, audio, video, etc.
# file operations, network programming, etc.
# bytes is a memory efficient sequence of bytes.

# 1 byte = 8 bits every bit can be 0 or 1
# 1 KB = 1024 bytes | 1 KB = 1024 * 8 bits
# 1 MB = 1024 KB | 1 MB = 1024 * 1024 * 8 bits
# 1 GB = 1024 MB | 1 GB = 1024 * 1024 * 1024 * 8 bits
# 1 TB = 1024 GB | 1 TB = 1024 * 1024 * 1024 * 1024 * 8 bits

# ===================== str (string) example =====================
# pure python string
text = "Hello World"
print(text)               # Hello World
print(type(text))         # <class 'str'>

# string to bytes
print(text.encode())      # b'Hello World'  → string to bytes
print(type(text.encode())) # <class 'bytes'>

# bytes to string (decode)
print(text.decode())      # Hello World  → bytes to string
print(type(text.decode())) # <class 'str'>

# string translation
table = str.maketrans("Helo", "HELO")
translated = text.translate(table)
print(translated)         # HELLO WORLD


# ===================== bytes example ============================

data = bytes([65, 66, 67, 68])
print(data)               # b'ABCD'
print(type(data))         # <class 'bytes'>

# bytes to string (decode)
decoded = data.decode()
print(decoded)            # ABCD

# Hex to bytes
hex_data = bytes.fromhex("48656c6c6f20576f726c64")
print(hex_data)           # b'Hello World'

# bytes-of every element show
for b in data:
    print(b, end=" ")     # 65 66 67 68


# ===================== what is bytes array ============================
# bytes array is an array of bytes.
# bytes array is mutable.
# bytes array is used for representing binary data.
# bytes array is used for representing image, audio, video, etc.
# file operations, network programming, etc.

# ===================== bytes array example ============================

data = bytearray([65, 66, 67, 68])
print(data)               # bytearray(b'ABCD')
print(type(data))         # <class 'bytearray'>

# bytes array to string (decode)
print(data.decode())      # ABCD

# bytes array-of every element show
for b in data:
    print(b, end=" ")     # 65 66 67 68
