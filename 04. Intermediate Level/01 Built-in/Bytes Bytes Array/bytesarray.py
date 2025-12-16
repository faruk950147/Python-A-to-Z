# ===================== bytearray in Python ============================
# bytearray is a mutable sequence of bytes (0–255)
# used for representing binary data. also used for representing image, audio, video, etc.
# file operations, network programming, etc.
# bytearray is a memory efficient sequence of bytes.

# 1 byte = 8 bits every bit can be 0 or 1
# 1 KB = 1024 bytes | 1 KB = 1024 * 8 bits
# 1 MB = 1024 KB | 1 MB = 1024 * 1024 * 8 bits
# 1 GB = 1024 MB | 1 GB = 1024 * 1024 * 1024 * 8 bits
# 1 TB = 1024 GB | 1 TB = 1024 * 1024 * 1024 * 1024 * 8 bits

# ===================== Constructor Examples ============================
data1 = bytearray([65, 66, 67, 68])
print(data1)                # bytearray(b'ABCD')

data2 = bytearray("Hello", "utf-8")
print(data2)                # bytearray(b'Hello')

# ===================== Mutable (changeable) ============================
data2[0] = 90               # 'H' -> 'Z' (ASCII 90)
print(data2)                # bytearray(b'Zello')

# ===================== Append, Extend, Insert ============================
data = bytearray(b"ABC")
data.append(68)             # Adds 'D'
print(data)                 # bytearray(b'ABCD')

data.extend([69, 70])       # Adds 'E', 'F'
print(data)                 # bytearray(b'ABCDEF')

data.insert(0, 88)          # Insert 'X' at index 0
print(data)                 # bytearray(b'XABCDEF')

# ===================== Remove, Pop, Clear ============================
data.remove(65)             # Removes first 'A' (65)
print(data)                 # bytearray(b'XBCDEF')

data.pop()                  # Removes last element 'F'
print(data)                 # bytearray(b'XBCDE')

data.clear()                # Removes all elements
print(data)                 # bytearray(b'')

# ===================== Recreate ============================
data = bytearray(b"banana")

# ===================== Slicing ============================
print(data[0:3])            # bytearray(b'ban')
data[0:3] = b"xxx"
print(data)                 # bytearray(b'xxxana')

# ===================== count(), find(), index() ============================
print(data.count(b"a"[0]))  # 3
print(data.find(b"x"[0]))   # 0
print(data.index(b"n"[0]))  # 4

# ===================== replace() ============================
print(data.replace(b"x", b"b"))  # bytearray(b'bbbanana')

# ===================== split() and join() ============================
print(b"one two three".split())  # [b'one', b'two', b'three']

# join works with bytes
joined = b"-".join([b"A", b"B", b"C"])
print(joined)                    # b'A-B-C'

# ===================== upper(), lower(), capitalize(), title() ============================
text = bytearray(b"hello world")
print(text.capitalize())         # bytearray(b'Hello world')
print(text.title())              # bytearray(b'Hello World')
print(text.upper())              # bytearray(b'HELLO WORLD')
print(text.lower())              # bytearray(b'hello world')

# ===================== strip(), lstrip(), rstrip() ============================
data = bytearray(b"***python***")
print(data.strip(b"*"))          # bytearray(b'python')
print(data.lstrip(b"*"))         # bytearray(b'python***')
print(data.rstrip(b"*"))         # bytearray(b'***python')

# ===================== startswith(), endswith() ============================
print(bytearray(b"data.txt").startswith(b"data"))  # True
print(bytearray(b"data.txt").endswith(b".txt"))    # True

# ===================== translate() and maketrans() ============================
table = bytes.maketrans(b"abc", b"xyz")
data = bytearray(b"abcde")
print(data.translate(table))      # bytearray(b'xyzde')

# ===================== decode() ============================
print(data.decode())              # xyzde

# ===================== comparison with bytes ============================
b1 = bytes("ABC", "utf-8")
b2 = bytearray("ABC", "utf-8")
print(b1 == b2)                   # True (content same)
b2[0] = 90
print(b2)                         # bytearray(b'ZBC')
# print(b1[0] = 90)  # TypeError: 'bytes' object does not support item assignment

# ===================== convert between bytes and bytearray ============================
b = bytes("Python", "utf-8")
ba = bytearray(b)
print(ba)                         # bytearray(b'Python')
print(bytes(ba))                  # b'Python'

# ===================== Built-in Functions ============================
data = bytearray(b"Python")
print(len(data))                  # 6
print(min(data))                  # 80 ('P')
print(max(data))                  # 121 ('y')
print(sum(data))                  # 642
print(list(data))                 # [80, 121, 116, 104, 111, 110]

# ===================== End ============================
print("All bytearray methods demonstrated successfully.")
