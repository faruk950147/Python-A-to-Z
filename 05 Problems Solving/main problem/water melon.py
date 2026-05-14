def water_melon(w):
    if w % 2 == 0 and w > 2:
        return "YES"
    else:
        return "NO"

print(water_melon(4))
print(water_melon(3))
print(water_melon(8))
print(water_melon(11))