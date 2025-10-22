# ===================== what is bytes ==========================
# bytes is an immutable sequence of bytes. 
# all elements of bytes must be in range(0, 256).
# used for representing binary data. also used for representing image, audio, video, etc.
# file operations, network programming, etc.

# ===================== how to create bytes =====================
# ===================== str (string) example =====================

text = "Hello World"
print(text)               # Hello World
print(type(text))         # <class 'str'>
print(text.encode())      # b'Hello World'  → string থেকে bytes

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
