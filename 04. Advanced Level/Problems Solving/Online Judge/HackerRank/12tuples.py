def calculate_hash(n, integer_list):
    # integer_list to tuple-
    integer_tuple = tuple(integer_list)
    print(hash(integer_tuple))  # tuple 

if __name__ == "__main__":
    n = int(input())
    integer_list = list(map(int, input().split()))
    calculate_hash(n, integer_list)


if __name__ == "__main__":
    n = int(input())
    integer_list = map(int, input().split())  
    integer_tuple = tuple(integer_list)
    print(hash(integer_tuple))




# my_tuple = (1, 2, [3, 4, 5])
# print(my_tuple)          # (1, 2, [3, 4, 5])

# # List modify the tuple
# my_tuple[2][0] = 10
# print(my_tuple)          # (1, 2, [10, 4, 5])


# my_tuple = (1, {"name": "Rafi"}, 3)
# print(my_tuple)         # (1, {'name': 'Rafi'}, 3)

# # Dict modify the tuple
# # Note: This is not a good practice, but it works in Python
# my_tuple[1]["name"] = "Hasan"
# print(my_tuple)         # (1, {'name': 'Hasan'}, 3)
