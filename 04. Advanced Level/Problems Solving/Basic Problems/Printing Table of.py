def table_of(num):
    for i in range(1, 11):
        print(f"it's table of square {num} x {i} = {num * i}")

table_of(5)

def table_of_2d(num):
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"it's table of square {num} x {i} x {j} = {num * i * j}")
table_of_2d(5)