data = [10, 20, 30, 40, 50]
i = 0

# Traverse loop
while (i := i + 1) < (n := len(data)):
    print(f"traverse {i} : {data[i]}")

# Pop loop
while len(data) > 0:
    print(f"pop {i} : {data.pop()}")
    i += 1