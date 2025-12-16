# zfill()
# zfill() is used to fill the string with zeros and return a string

def zfill_str(word):
    return word.zfill(10)

print(zfill_str("123")) # 00000123
print(zfill_str("-123")) # -123
print(zfill_str("+123")) # +123
print(zfill_str("123.45")) # 000123.45
