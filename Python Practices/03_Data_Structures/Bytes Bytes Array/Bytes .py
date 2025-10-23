# ===================== what is bytes ============================
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

# ===================== Constructor Examples ============================
data1 = bytes([65, 66, 67, 68])
print(data1)                # b'ABCD'

data2 = bytes("Hello", encoding="utf-8")
print(data2)                # b'Hello'

# ===================== Common Properties ============================
print(len(data2))            # 5
print(type(data2))           # <class 'bytes'>
print(list(data2))           # [72, 101, 108, 108, 111]

# ===================== Indexing and Slicing ============================
print(data2[0])              # 72 (ASCII of 'H')
print(data2[1:4])            # b'ell'

# ===================== Built-in Functions ============================
print(len(data2))            # 5
print(min(data2))            # 72
print(max(data2))            # 111
print(sum(data2))            # 508

# ===================== count(), find(), index() ============================
data = b"banana"
print(data.count(b"a"))      # 3
print(data.find(b"a"))       # 1
print(data.index(b"n"))      # 2

# ===================== replace() ============================
print(data.replace(b"a", b"x"))   # b'bxnxnx'

# ===================== split() and rsplit() ============================
print(b"hello world python".split())        # [b'hello', b'world', b'python']
print(b"one two three".rsplit(b" ", 1))     # [b'one two', b'three']

# ===================== join() ============================
joined = b"-".join([b"A", b"B", b"C", b"D"])
print(joined)                 # b'A-B-C-D'

# ===================== capitalize(), title(), upper(), lower(), swapcase() ============================
text = b"hello world"
print(text.capitalize())      # b'Hello world'
print(text.title())           # b'Hello World'
print(text.upper())           # b'HELLO WORLD'
print(text.lower())           # b'hello world'
print(b"HeLLo".swapcase())    # b'hEllO'

# ===================== strip(), lstrip(), rstrip() ============================
data = b"***python***"
print(data.strip(b"*"))       # b'python'
print(data.lstrip(b"*"))      # b'python***'
print(data.rstrip(b"*"))      # b'***python'

# ===================== startswith(), endswith() ============================
print(b"data.txt".startswith(b"data"))      # True
print(b"data.txt".endswith(b".txt"))        # True

# ===================== partition() and rpartition() ============================
print(b"key=value".partition(b"="))         # (b'key', b'=', b'value')
print(b"a=b=c".rpartition(b"="))            # (b'a=b', b'=', b'c')

# ===================== isalpha(), isdigit(), isalnum(), isspace() ============================
print(b"abc".isalpha())       # True
print(b"123".isdigit())       # True
print(b"abc123".isalnum())    # True
print(b"   ".isspace())       # True

# ===================== center(), zfill() ============================
print(b"Hi".center(8, b"*"))  # b'***Hi***'
print(b"42".zfill(6))         # b'000042'

# ===================== translate() and maketrans() ============================
table = bytes.maketrans(b"abc", b"xyz")
print(b"abcde".translate(table))   # b'xyzde'

# ===================== decode() ============================
data = bytes("Bangla", "utf-8")
print(data.decode())               # Bangla

# ===================== Additional Built-in Functions ============================
data = b"Python"
print(len(data))                   # 6
print(min(data))                   # 80 ('P')
print(max(data))                   # 121 ('y')
print(sum(data))                   # 642
print(list(data))                  # [80, 121, 116, 104, 111, 110]

# ===================== bytes immutability check ============================
try:
    data[0] = 65   # Error: bytes is immutable
except TypeError as e:
    print(e)

# ===================== Practical Example ============================
# Suppose we read binary file (simulated)
binary_data = bytes([255, 0, 127, 100])
print(binary_data)                 # b'\xff\x00\x7fd'

# Converting to hex string
print(binary_data.hex())           # 'ff007f64'

# ===================== End ============================
print("All bytes methods demonstrated successfully.")
