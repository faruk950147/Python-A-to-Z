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

# ===================== bytes constructor ============================
data = bytes([65, 66, 67, 68])
print(data)               # b'ABCD'
print(type(data))         # <class 'bytes'>

# ===================== bytes constructor with string 
# ============================
data = bytes("ABCD", encoding="utf-8")
print(data)               # b'ABCD'
print(type(data))         # <class 'bytes'>

print(data.index(b'A'))      # 0
print(data.index(b'B'))      # 1
print(data.index(b'C'))      # 2
print(data.index(b'D'))      # 3
